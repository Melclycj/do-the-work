"""README schema enumeration — the F3 mechanization from the `1df6245` cold read.

The instruction layer's navigation surface (document-harness/README.md) decayed silently
when W2 added `review.v2.schema.json`: the directory held 14 schema files, the README
table enumerated 13, and no instrument noticed until a node-boundary cold read (finding
3 — the decay class, not one instance: W1's `document-work-spec.v2` only avoided it
because that round happened to edit the README by hand). This guard closes the class:
every `*.schema.json` under `schema/document-assurance-v3/` must be mentioned by stem in
the README.

It deliberately reads instruction prose — the one named exception to the layer's
"no test reads it" property; both operating contracts carry the exception alongside this
test's addition (same commit), so the property statement stays true as qualified.

The expectation (hand-written README text) is independent of the source (the directory
listing), and the guard was proven red before the README row it pins was added
(`review.v2` absent -> exactly this failure, reproduced at authoring time). After the
`39e4136` checkpoint read's F2 (bare substring matching satisfiable by unrelated prose),
matching was narrowed to delimited tokens and re-proven red in three directions
(review.v2 / [review] / [assurance] entry each removed -> red). Matching is deliberately
whole-README rather than scoped to the table region the ruled minimum fix named: all 14
delimited stems sit in the three enumeration rows today, so the two are equivalent, and a
region parser is new machinery for zero current value — disclosed per checkpoint read
`43fb1c5` cr-F2.
"""
from __future__ import annotations

import pathlib
import unittest


class ReadmeSchemaEnumeration(unittest.TestCase):
    def test_every_schema_file_is_named_in_the_readme(self) -> None:
        root = pathlib.Path(__file__).resolve().parents[4]
        schema_dir = root / "ResearchSystem" / "schema" / "document-assurance-v3"
        readme = root / "ResearchSystem" / "document-harness" / "README.md"
        stems = sorted(
            p.name[: -len(".schema.json")] for p in schema_dir.glob("*.schema.json")
        )
        # An empty listing would make the loop below pass over nothing — the vacuous-guard
        # shape the dispatch-generator rounds paid to delete. Refuse it explicitly.
        self.assertTrue(stems, "schema directory listing came back empty — guard is vacuous")
        text = readme.read_text(encoding="utf-8")
        # Delimited-token matching: the stem must appear as a code span (`stem`) or a
        # link text ([stem]) — the two forms the README's enumeration rows use. Bare
        # `stem in text` was mutation-proven satisfiable by unrelated prose (checkpoint
        # read 39e4136 F2: deleting the [review] and [assurance] entries stayed green,
        # satisfied by "review round" prose and "document-work-assurance-v3" paths).
        missing = [
            stem
            for stem in stems
            if f"`{stem}`" not in text and f"[{stem}]" not in text
        ]
        self.assertEqual(
            missing,
            [],
            "schema files not mentioned in document-harness/README.md "
            f"'Authoritative documents' table: {missing}",
        )


if __name__ == "__main__":
    unittest.main()
