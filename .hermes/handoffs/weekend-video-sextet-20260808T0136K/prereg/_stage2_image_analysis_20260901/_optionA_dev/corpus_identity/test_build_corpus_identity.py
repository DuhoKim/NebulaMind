import csv, json, unittest, tempfile, hashlib, sys
from datetime import datetime, timezone, timedelta
from unittest import mock
from pathlib import Path
import numpy as np
import build_corpus_identity as m
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'beacon_v2'))
import beacon_record as br, drand_round, test_pki as pki
from datetime import datetime, timezone, timedelta

class CorpusIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.out=Path(tempfile.mkdtemp()); cls.ok=m.build(out_dir=cls.out)      # writes NOTHING into the lane: the sealed identity is produced once, after signature

    def fetched_record(self, source='nist'):
        """A GENUINE record from beacon_record.collect over the three-tier test network; returns the network so builds re-fetch from the same source."""
        d=Path(tempfile.mkdtemp()); rec=d/'record.json'; stmt=d/'statement.txt'; D='a'*64
        t_sign=datetime(2026,9,6,0,0,tzinfo=timezone.utc); tp=br.pulse_time(t_sign); stmt.write_bytes(f'signed {D} at {br.fmt(t_sign)}'.encode())
        if source=='nist': net=pki.network(tp); now=tp+timedelta(hours=1)
        else: net=pki.network(tp, nist_404=True, drand=(drand_round.round_for(tp),'f'*64)); now=tp+timedelta(hours=25)
        R=br.collect(net, br.fmt(t_sign), D, stmt.read_bytes(), now=now); rec.write_text(json.dumps(R)); self._net=net; self._now=now
        return rec,stmt,D
    def bld(self, **kw):
        m.nist_pulse.pinned_roots=lambda: pki.roots()          # test root in place of the pinned DigiCert root (production: the pinned file)
        return m.build(fetch=self._net, now=self._now, **kw)
    def assert_refusal(self, token, rec, stmt, D):
        with self.assertRaises(SystemExit) as cm: self.bld(out_dir=Path(tempfile.mkdtemp()),beacon_record_path=rec,exclude_path=Path(__file__).with_name('dryrun_identities_to_exclude_20260905.txt'),rule_sha256=D,signature_statement=stmt)
        self.assertIn(token,str(cm.exception))

    def test_real_validation_control(self):
        # §9B.5 control: the 2,000 smallest h mod 2^32 of the guarded pool ARE the failed set (VALIDATION_SELECTION_V29),
        # compared as a SET with equal labels — that CSV is written in GZ1_OBJID order, not rank order. The build must PASS.
        self.assertTrue(self.ok)
        with open(m.ROOT/'VALIDATION_SELECTION_V29_20260905.csv',newline='') as f:
            frozen={int(r['GZ1_OBJID']):int(float(r['G'])) for r in csv.DictReader(f)}
        with open(Path(__file__).with_name('guarded_pool.csv'),newline='') as f:
            pool=[{'objid':int(r['GZ1_OBJID']),'ra':float(r['RA']),'dec':float(r['DEC']),'g':int(r['G'])} for r in csv.DictReader(f)]
        top=m.order_rows(pool)[:2000]
        self.assertEqual({r['objid'] for r in top}, set(frozen)); self.assertTrue(all(frozen[r['objid']]==r['g'] for r in top))
        I=json.loads(Path(self.out/'corpus_identity.json').read_text())
        self.assertEqual((len(I['tuning_objids']),len(I['holdout_objids']),len(I['fresh_validation_objids'])),(400,200,2000))   # DRIVER schema, flat keys
        self.assertEqual((I['detail']['tuning']['count'],I['detail']['holdout']['count'],I['detail']['fresh_validation']['count']),(400,200,2000))
        self.assertEqual(I['schema_version'],'CORPUS-IDENTITY-2'); self.assertIn('renderability_inputs',I)
        ids=I['tuning_objids']+I['holdout_objids']+I['fresh_validation_objids']
        self.assertEqual(len(set(ids)),2600); self.assertFalse(set(ids)&set(frozen))                       # disjoint from the failed set and from each other
        self.assertTrue(all(r['rank']>2000 for r in I['skipped_non_renderable']))

    def test_beacon_split_deterministic_excludes_and_differs(self):
        ex=Path(__file__).with_name('dryrun_identities_to_exclude_20260905.txt'); rec,stmt,D=self.fetched_record('nist'); out1=Path(tempfile.mkdtemp()); out2=Path(tempfile.mkdtemp())
        thin=out1/'thin.json'; thin.write_text(json.dumps({'source':'NIST-beacon-2.0','seed_hex':'e'*128,'T_pulse':'test'}))
        self.assert_refusal('BEACON-NOT-ACCEPTED',thin,stmt,D)                                                        # a hand-made record: verdict REFUSE-SCHEMA
        self.assertTrue(self.bld(out_dir=out1, beacon_record_path=rec, exclude_path=ex,rule_sha256=D,signature_statement=stmt))
        A=json.loads((out1/'corpus_identity.json').read_text()); seed=A['seed_hex']; self.assertEqual(len(seed),128); self.assertEqual(A['beacon_outcome'],'ACCEPT-NIST'); self.assertEqual(A['beacon_record_sha256'], m.hashlib.sha256(rec.read_bytes()).hexdigest()); self.assertEqual(A['rule_sha256'],D)
        self.assertTrue(m.build(out_dir=out2, seed_hex=seed.upper(), exclude_path=ex, test_seed=True)); B=json.loads((out2/'corpus_identity.json').read_text())
        self.assertEqual(A['tuning_objids'],B['tuning_objids']); self.assertEqual(B['split_mode'][:9],'TEST-SEED')                          # same seed (case-insensitive) -> same split; test-seed is marked
        with self.assertRaises(SystemExit): m.build(out_dir=Path(tempfile.mkdtemp()), seed_hex=seed, exclude_path=ex)                          # bare seed without --test-seed refused
        excluded={int(x) for x in ex.read_text().split()}
        with open(m.ROOT/'VALIDATION_SELECTION_V29_20260905.csv', newline='') as _fh: frozen={int(r['GZ1_OBJID']) for r in csv.DictReader(_fh)}
        ids=A['tuning_objids']+A['holdout_objids']+A['fresh_validation_objids']; self.assertEqual(len(set(ids)),2600); self.assertFalse(set(ids)&excluded); self.assertFalse(set(ids)&frozen)
        self.assertEqual(A['excluded_count'],len(excluded)); self.assertEqual(A['split_mode'][:13],'beacon-seeded')
        Dd=json.loads((self.out/'corpus_identity.json').read_text()); self.assertNotEqual(A['tuning_objids'], Dd['tuning_objids'])          # differs from the deterministic dry-run order
        other=Path(tempfile.mkdtemp()); self.assertTrue(m.build(out_dir=other, seed_hex='0'*64, exclude_path=ex, test_seed=True)); O=json.loads((other/'corpus_identity.json').read_text()); self.assertNotEqual(A['tuning_objids'],O['tuning_objids'])
    def test_fetcher_records_nist_and_drand_and_negative_bindings(self):
        ex=Path(__file__).with_name('dryrun_identities_to_exclude_20260905.txt')
        for source in ('nist','drand'):
            rec,stmt,D=self.fetched_record(source); out=Path(tempfile.mkdtemp())
            self.assertTrue(self.bld(out_dir=out,beacon_record_path=rec,exclude_path=ex,rule_sha256=D,signature_statement=stmt))
            I=json.loads((out/'corpus_identity.json').read_text()); self.assertEqual(I['beacon_outcome'], 'ACCEPT-NIST' if source=='nist' else 'ACCEPT-DRAND'); self.assertEqual(len(I['seed_hex']), 128 if source=='nist' else 64)
        rec,stmt,D=self.fetched_record('nist')
        with self.assertRaises(SystemExit) as cm: self.bld(out_dir=Path(tempfile.mkdtemp()),beacon_record_path=rec,exclude_path=ex,rule_sha256='b'*64,signature_statement=stmt)
        self.assertIn('REFUSE-RULE-DIGEST', str(cm.exception))                                                                                  # the shared verdict's token surfaces in the builder's refusal
        bad=rec.parent/'bad.txt'; bad.write_bytes(b'unrelated statement')
        with self.assertRaises(SystemExit) as cm: self.bld(out_dir=Path(tempfile.mkdtemp()),beacon_record_path=rec,exclude_path=ex,rule_sha256=D,signature_statement=bad)
        self.assertIn('REFUSE-STATEMENT-BYTES', str(cm.exception))
        q=json.loads(rec.read_text()); q['nist']['intermediate_pems_b64']=[]; p=rec.parent/'nointer.json'; p.write_text(json.dumps(q))            # chain without its intermediate: not anchored -> RETRY -> not accepted
        with self.assertRaises(SystemExit) as cm: self.bld(out_dir=Path(tempfile.mkdtemp()),beacon_record_path=p,exclude_path=ex,rule_sha256=D,signature_statement=stmt)
        self.assertIn('BEACON-NOT-ACCEPTED', str(cm.exception))
    def test_small_ordering_and_renderability(self):
        rows=[{'objid':x,'ra':float(x),'dec':0.0,'g':1} for x in (4,1,3,2)]
        ordered=m.order_rows(rows)
        expected=sorted(rows,key=lambda r:(int.from_bytes(__import__('hashlib').sha256(str(r['objid']).encode('ascii')).digest(),'big')%(2**32),r['objid']))
        self.assertEqual([x['objid'] for x in ordered],[x['objid'] for x in expected])
        bricks={'name':np.array(['a','b']),'ra1':np.array([0.,2.]),'ra2':np.array([2.,4.]),'dec1':np.array([-1.,-1.]),'dec2':np.array([1.,1.])}
        custom=[{'objid':1,'ra':0.5,'dec':0.,'g':1},{'objid':2,'ra':2.5,'dec':0.,'g':-1},{'objid':3,'ra':9.,'dec':0.,'g':1},{'objid':4,'ra':1.5,'dec':0.,'g':1}]
        groups,skipped,last=m.classify(custom,bricks,{'b'},counts=(1,1))
        self.assertEqual([[r['objid'] for r in g] for g in groups],[[1],[4]])
        self.assertEqual([r['reason'] for r in skipped],['NO_PUBLISHED_R_COVERAGE','NO_DR9N_BRICK']); self.assertEqual(last,4)

if __name__=='__main__': unittest.main()
