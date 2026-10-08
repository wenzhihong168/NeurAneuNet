# Release Checklist

Complete this checklist before publishing a NeurAneuNet result, model artifact, or implementation update.

## Evidence

- [ ] Cohort criteria and the 600-case, 210-PED, and independent 21-case roles remain explicit.
- [ ] Patient-level split and annotation versions are frozen and hashed.
- [ ] Segmentation, geometry, device, landing-zone, and clinical outcomes are reported separately.
- [ ] Tables and figures resolve to the artifact manifest and evaluated checkpoints.
- [ ] Claims distinguish published results from reproduced or newly estimated values.

## Clinical and privacy review

- [ ] No image, identifier, acquisition header, free text, or private path is exposed.
- [ ] Device recommendations are presented as research outputs, not autonomous clinical advice.
- [ ] Severe failures and out-of-distribution cases have been reviewed.
- [ ] Independent clinical cases were not used for model or threshold selection.

## Repository quality

- [ ] Configuration, environment, seeds, units, and metric versions are recorded.
- [ ] Public examples are synthetic or separately approved.
- [ ] Documentation and citation metadata match the released scope.
- [ ] Generated data, checkpoints, logs, and credentials are excluded.
- [ ] The tagged revision reproduces every public-safe result artifact.
