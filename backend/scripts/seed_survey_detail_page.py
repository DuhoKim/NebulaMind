"""Load Survey Detail Page v1 seeds.

Order is part of the contract:
1. survey_datasets_backfill.json
2. survey_releases/*.json
3. catalog_fields/*.json
"""
from __future__ import annotations

import json
import argparse
from pathlib import Path

from sqlalchemy import text

from app.database import SessionLocal


SEED_ROOT = Path(__file__).resolve().parents[1] / "seeds"
CATALOG_DATASET_SLUG_MAP = {
    "erosita-dr1": "erosita-erass1",
}


def load_json(path: Path):
    return json.loads(path.read_text())


def resolve_seed_paths(subdir: str, names: list[str] | None) -> list[Path]:
    root = SEED_ROOT / subdir
    if not names:
        return sorted(root.glob("*.json"))
    paths: list[Path] = []
    for name in names:
        path = Path(name)
        if not path.is_absolute():
            path = root / path
        if path.suffix != ".json":
            path = path.with_suffix(".json")
        paths.append(path)
    return paths


def load_dataset_backfill() -> tuple[int, int]:
    payload = load_json(SEED_ROOT / "survey_datasets_backfill.json")
    inserted_or_updated = 0
    patched = 0

    with SessionLocal() as db:
        for row in payload.get("new", []):
            survey = db.execute(
                text("SELECT id FROM surveys WHERE slug = :slug"),
                {"slug": row["survey_slug"]},
            ).fetchone()
            if not survey:
                print(f"SKIP dataset {row['slug']}: survey {row['survey_slug']} not found")
                continue

            db.execute(
                text(
                    """
                    INSERT INTO survey_datasets (
                        survey_id, slug, name, full_name, description, data_type,
                        release_year, release_label, redshift_range, sky_coverage_deg2,
                        sample_size, doi, primary_url, archive_url, bibcode,
                        registry, license, status
                    )
                    VALUES (
                        :survey_id, :slug, :name, :full_name, :description, :data_type,
                        :release_year, :release_label, :redshift_range, :sky_coverage_deg2,
                        :sample_size, :doi, :primary_url, :archive_url, :bibcode,
                        :registry, :license, :status
                    )
                    ON CONFLICT (slug) DO UPDATE SET
                        survey_id = EXCLUDED.survey_id,
                        name = EXCLUDED.name,
                        full_name = EXCLUDED.full_name,
                        description = EXCLUDED.description,
                        data_type = EXCLUDED.data_type,
                        release_year = EXCLUDED.release_year,
                        release_label = EXCLUDED.release_label,
                        redshift_range = EXCLUDED.redshift_range,
                        sky_coverage_deg2 = EXCLUDED.sky_coverage_deg2,
                        sample_size = EXCLUDED.sample_size,
                        primary_url = EXCLUDED.primary_url,
                        archive_url = EXCLUDED.archive_url,
                        registry = EXCLUDED.registry,
                        license = EXCLUDED.license,
                        status = EXCLUDED.status,
                        doi = COALESCE(survey_datasets.doi, EXCLUDED.doi),
                        bibcode = COALESCE(survey_datasets.bibcode, EXCLUDED.bibcode),
                        updated_at = NOW()
                    """
                ),
                {
                    "survey_id": survey.id,
                    "slug": row["slug"],
                    "name": row["name"],
                    "full_name": row["full_name"],
                    "description": row["description"],
                    "data_type": row["data_type"],
                    "release_year": row.get("release_year"),
                    "release_label": row.get("release_label"),
                    "redshift_range": row.get("redshift_range"),
                    "sky_coverage_deg2": row.get("sky_coverage_deg2"),
                    "sample_size": row.get("sample_size"),
                    "doi": row.get("doi"),
                    "primary_url": row["primary_url"],
                    "archive_url": row.get("archive_url"),
                    "bibcode": row.get("bibcode"),
                    "registry": row.get("registry"),
                    "license": row.get("license"),
                    "status": row.get("status", "active"),
                },
            )
            inserted_or_updated += 1

        for row in payload.get("updates", []):
            result = db.execute(
                text(
                    """
                    UPDATE survey_datasets
                    SET doi = COALESCE(doi, :doi),
                        bibcode = COALESCE(bibcode, :bibcode),
                        updated_at = NOW()
                    WHERE slug = :slug
                    """
                ),
                {"slug": row["slug"], "doi": row.get("doi"), "bibcode": row.get("bibcode")},
            )
            patched += result.rowcount or 0

        db.commit()

    return inserted_or_updated, patched


def load_releases(paths: list[Path] | None = None) -> int:
    count = 0
    with SessionLocal() as db:
        for path in paths or sorted((SEED_ROOT / "survey_releases").glob("*.json")):
            payload = load_json(path)
            survey = db.execute(
                text("SELECT id FROM surveys WHERE slug = :slug"),
                {"slug": payload["survey_slug"]},
            ).fetchone()
            if not survey:
                print(f"SKIP releases {path.name}: survey {payload['survey_slug']} not found")
                continue

            retire_labels = payload.get("retire_labels") or []
            if retire_labels:
                result = db.execute(
                    text(
                        """
                        DELETE FROM survey_data_releases
                        WHERE survey_id = :survey_id
                          AND label = ANY(:retire_labels)
                        """
                    ),
                    {"survey_id": survey.id, "retire_labels": retire_labels},
                )
                retired = result.rowcount or 0
                if retired:
                    print(f"retired {path.name}: {retired} stale release rows")

            for row in payload.get("releases", []):
                db.execute(
                    text(
                        """
                        INSERT INTO survey_data_releases (
                            survey_id, label, release_date, release_year, summary,
                            n_objects, sky_coverage_deg2, data_volume_tb, doi,
                            bibcode, url, status
                        )
                        VALUES (
                            :survey_id, :label, :release_date, :release_year, :summary,
                            :n_objects, :sky_coverage_deg2, :data_volume_tb, :doi,
                            :bibcode, :url, :status
                        )
                        ON CONFLICT (survey_id, label) DO UPDATE SET
                            release_date = EXCLUDED.release_date,
                            release_year = EXCLUDED.release_year,
                            summary = EXCLUDED.summary,
                            n_objects = EXCLUDED.n_objects,
                            sky_coverage_deg2 = EXCLUDED.sky_coverage_deg2,
                            data_volume_tb = EXCLUDED.data_volume_tb,
                            doi = EXCLUDED.doi,
                            bibcode = EXCLUDED.bibcode,
                            url = EXCLUDED.url,
                            status = EXCLUDED.status,
                            updated_at = NOW()
                        """
                    ),
                    {
                        "survey_id": survey.id,
                        "label": row["label"],
                        "release_date": row.get("release_date"),
                        "release_year": row.get("release_year"),
                        "summary": row["summary"],
                        "n_objects": row.get("n_objects"),
                        "sky_coverage_deg2": row.get("sky_coverage_deg2"),
                        "data_volume_tb": row.get("data_volume_tb"),
                        "doi": row.get("doi"),
                        "bibcode": row.get("bibcode"),
                        "url": row.get("url"),
                        "status": row.get("status", "released"),
                    },
                )
                count += 1

        db.commit()

    return count


def load_catalog_fields(paths: list[Path] | None = None) -> int:
    count = 0
    with SessionLocal() as db:
        for path in paths or sorted((SEED_ROOT / "catalog_fields").glob("*.json")):
            payload = load_json(path)
            seed_slug = payload["dataset_slug"]
            dataset_slug = CATALOG_DATASET_SLUG_MAP.get(seed_slug, seed_slug)
            dataset = db.execute(
                text("SELECT id FROM survey_datasets WHERE slug = :slug"),
                {"slug": dataset_slug},
            ).fetchone()
            if not dataset:
                print(f"SKIP fields {path.name}: dataset {dataset_slug} not found")
                continue

            source_url = payload["source_url"]
            for row in payload.get("fields", []):
                db.execute(
                    text(
                        """
                        INSERT INTO survey_catalog_fields (
                            dataset_id, name, dtype, unit, description, example,
                            is_key, sort_order, source_url
                        )
                        VALUES (
                            :dataset_id, :name, :dtype, :unit, :description, :example,
                            :is_key, :sort_order, :source_url
                        )
                        ON CONFLICT (dataset_id, name) DO UPDATE SET
                            dtype = EXCLUDED.dtype,
                            unit = EXCLUDED.unit,
                            description = EXCLUDED.description,
                            example = EXCLUDED.example,
                            is_key = EXCLUDED.is_key,
                            sort_order = EXCLUDED.sort_order,
                            source_url = EXCLUDED.source_url
                        """
                    ),
                    {
                        "dataset_id": dataset.id,
                        "name": row["name"],
                        "dtype": row.get("dtype"),
                        "unit": row.get("unit"),
                        "description": row["description"],
                        "example": row.get("example"),
                        "is_key": bool(row.get("is_key", False)),
                        "sort_order": row.get("sort_order", 0),
                        "source_url": source_url,
                    },
                )
                count += 1

        db.commit()

    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-datasets",
        action="store_true",
        help="Skip survey_datasets_backfill.json.",
    )
    parser.add_argument(
        "--release-file",
        action="append",
        dest="release_files",
        help="Specific survey_releases seed file to load, by basename or path. Repeatable.",
    )
    parser.add_argument(
        "--catalog-field-file",
        action="append",
        dest="catalog_field_files",
        help="Specific catalog_fields seed file to load, by basename or path. Repeatable.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.skip_datasets:
        print("survey_datasets_backfill: skipped")
    else:
        datasets, patches = load_dataset_backfill()
        print(f"survey_datasets_backfill: {datasets} upserts, {patches} NULL-only doi/bibcode patches")

    release_paths = resolve_seed_paths("survey_releases", args.release_files)
    releases = load_releases(release_paths)
    print(f"survey_releases: {releases} upserts")

    catalog_field_paths = resolve_seed_paths("catalog_fields", args.catalog_field_files)
    fields = load_catalog_fields(catalog_field_paths)
    print(f"catalog_fields: {fields} upserts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
