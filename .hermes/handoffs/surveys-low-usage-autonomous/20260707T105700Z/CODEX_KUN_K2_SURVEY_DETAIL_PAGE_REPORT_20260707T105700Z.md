# Codex/Kun K2 Survey detail page audit report

Marker: `CODEX_KUN_K2_SURVEY_DETAIL_PAGE_REPORT_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Status: PASS_WITH_FINDINGS

## Files inspected

- `frontend/src/app/surveys/[slug]/page.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
- `backend/app/routers/surveys.py`
- `backend/app/models/survey.py`
- `docs/survey_detail_page_v1.md`
- `docs/autowiki_surveys_v1.md`

## Commands run

- `sed -n ...` / `nl -ba ...` read-only inspections of the files above.
- `rg -n "test:surveys-atlas-ia|surveys" frontend/package.json frontend -g 'package.json' -g '*test*'`
- `cd frontend && npm run test:surveys-atlas-ia`
  - Result: PASS, output `surveys atlas IA smoke checks passed`.

No servers were started and no production DB/API was contacted.

## Answers to specific questions

1. Data Releases, Data Products & Catalogs, News & Events, related wiki pages, and ideas are implemented in the current detail page. Data releases are rendered inline from `/api/surveys/{slug}`; datasets and events are fetched from secondary read-only endpoints; ideas and related wiki links are shown when counts/slugs exist.
2. Backend release/dataset helpers degrade safely for missing release/dataset/catalog tables via try/except. Client-side secondary fetches are weaker: datasets, events, and ideas lack `.catch()` handling, so network/runtime failures can leave console unhandled rejections or no explicit fallback state.
3. UI mostly matches the design: current release badge, planned dimming, empty release state, dataset accordions, key-field-first tables, DOI/ADS links, and catalog empty state are present. Two drift points: catalogs render/fetch even when `datasets_count === 0`, while the design said render only when datasets exist; >15 visible field filter is not implemented.
4. Likely bugs/risks: secondary client fetch rejection handling; unconditional catalog fetch/section; related wiki page titles are discarded and reconstructed from slug; direct `/events` endpoint is less table-missing-tolerant than the main detail response.
5. Top 3 low-risk next changes: add catch/fallbacks to secondary client fetches; gate catalog fetch/section on `datasets_count > 0`; return/display related wiki page titles from the detail response.

## Findings

### High

None found in artifact-only inspection. The page has the intended core sections and the allowed smoke test passed.

### Medium

1. Secondary client fetches do not catch rejected requests.
   - Evidence: `SurveyDetailClient.tsx:576-578`, `SurveyDetailClient.tsx:588-591`, `SurveyDetailClient.tsx:602-605`.
   - Impact: if `/ideas`, `/datasets`, or `/events` rejects rather than returning a non-OK response, the page can produce unhandled promise noise and silently fail to show the designed empty state. The dataset/events `.finally()` will clear loading, but the rejection is still rethrown.

2. Direct events endpoint is not fully missing-table-safe.
   - Evidence: `backend/app/routers/surveys.py:266-314`.
   - Impact: the main page usually avoids this if `_get_survey_facility_profiles()` returns `[]`, but a direct call to `/api/surveys/{slug}/events` can 500 if `survey_facility_links`, `facility_profiles`, or `facility_news_items` is absent. This is less robust than the release/dataset helpers.

### Low

1. Catalog section does not follow the design's "render only when `datasets_count > 0`" rule.
   - Evidence: `SurveyDetailClient.tsx:317-334`, `SurveyDetailClient.tsx:584-592`, `SurveyDetailClient.tsx:773-774`.
   - Impact: surveys with zero dataset rows still fetch `/datasets` and show a "No public catalog metadata available yet" section. It is honest, but it differs from the design and adds an unnecessary request.

2. Dataset field table lacks the >15-row substring filter called for by the design.
   - Evidence: `SurveyDetailClient.tsx:337-431`.
   - Impact: large catalogs can become harder to scan once T1/T2 fields are seeded.

3. Related wiki pages lose API titles.
   - Evidence: backend selects `wp.slug, wp.title` but returns only slugs at `backend/app/routers/surveys.py:236-245`; UI reconstructs display names from slugs at `SurveyDetailClient.tsx:863-879`.
   - Impact: title casing and page names can be wrong or less readable than the canonical wiki title.

## Exact proposed patches, not applied

### Patch A — make secondary fetches reject-safe

```diff
diff --git a/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx b/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx
@@
           fetch(`/api/surveys/${slug}/ideas?include_stale=0`)
             .then(r => r.ok ? r.json() : { ideas: [] })
-            .then(r => setIdeas((r.ideas || []).slice(0, 5)));
+            .then(r => setIdeas((r.ideas || []).slice(0, 5)))
+            .catch(() => setIdeas([]));
@@
     fetch(`/api/surveys/${slug}/datasets`)
       .then(r => r.ok ? r.json() : { datasets: [] })
       .then(d => setDatasets(d.datasets || []))
+      .catch(() => setDatasets([]))
       .finally(() => setDatasetsLoading(false));
@@
     fetch(`/api/surveys/${slug}/events?limit=8`)
       .then(r => r.ok ? r.json() : { events: [] })
       .then(d => setEvents(d.events || []))
+      .catch(() => setEvents([]))
       .finally(() => setEventsLoading(false));
```

### Patch B — skip catalog fetch/section when `datasets_count` is zero

```diff
diff --git a/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx b/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx
@@
   useEffect(() => {
     if (!slug || !survey) return;
+    if (survey.datasets_count <= 0) {
+      setDatasets([]);
+      setDatasetsLoading(false);
+      return;
+    }
     setDatasets([]);
@@
-      <DatasetCatalogs datasets={datasets} loading={datasetsLoading} expectedCount={survey.datasets_count} />
+      {survey.datasets_count > 0 && (
+        <DatasetCatalogs datasets={datasets} loading={datasetsLoading} expectedCount={survey.datasets_count} />
+      )}
```

### Patch C — return and render related wiki page titles

```diff
diff --git a/backend/app/routers/surveys.py b/backend/app/routers/surveys.py
@@
-        detail["related_wiki_page_slugs"] = [p.slug for p in page_rows]
+        detail["related_wiki_pages"] = [{"slug": p.slug, "title": p.title} for p in page_rows]
+        detail["related_wiki_page_slugs"] = [p.slug for p in page_rows]
@@
     except Exception:
+        detail["related_wiki_pages"] = []
         detail["related_wiki_page_slugs"] = []
diff --git a/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx b/frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx
@@
   related_wiki_page_slugs: string[];
+  related_wiki_pages?: { slug: string; title: string }[];
@@
-      {survey.related_wiki_page_slugs.length > 0 && (
+      {(survey.related_wiki_pages?.length || survey.related_wiki_page_slugs.length) > 0 && (
@@
-            {survey.related_wiki_page_slugs.map(ps => (
-              <Link key={ps} href={`/wiki/${ps}`} style={{
+            {(survey.related_wiki_pages || survey.related_wiki_page_slugs.map(slug => ({ slug, title: slug.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase()) }))).map(page => (
+              <Link key={page.slug} href={`/wiki/${page.slug}`} style={{
@@
-                {ps.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
+                {page.title}
```

### Patch D — wrap `/events` endpoint in a graceful degradation guard

```diff
diff --git a/backend/app/routers/surveys.py b/backend/app/routers/surveys.py
@@
-    linked = db.execute(text("""
+    try:
+        linked = db.execute(text("""
         SELECT count(*)
         FROM survey_facility_links
         WHERE survey_id = :sid
-    """), {"sid": survey_row.id}).scalar() or 0
+        """), {"sid": survey_row.id}).scalar() or 0
+    except Exception:
+        return {"survey": {"slug": survey_row.slug, "name": survey_row.name}, "count": 0, "events": []}
@@
-    count = int(db.execute(text("""
+    try:
+        count = int(db.execute(text("""
@@
-    """), params).scalar() or 0)
+        """), params).scalar() or 0)
@@
-    rows = db.execute(text("""
+        rows = db.execute(text("""
@@
-    """), {**params, "limit": limit}).fetchall()
+        """), {**params, "limit": limit}).fetchall()
+    except Exception:
+        return {"survey": {"slug": survey_row.slug, "name": survey_row.name}, "count": 0, "events": []}
```

## Safety ledger

- Product files edited: 0
- DB writes / SQL / migrations: 0
- Deploy / restart / service mutation: 0
- Git commit / push / merge: 0
- Wiki/page publish: 0
- Cron: 0
- Browser automation: 0
- Provider/account/billing/API/GCP/OAuth/token/credential activity: 0
- Report written: `.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K2_SURVEY_DETAIL_PAGE_REPORT_20260707T105700Z.md`
