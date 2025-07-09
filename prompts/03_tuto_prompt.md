# Instructions: GitLab Docker Pipeline Tutorial with Process Tracking

Create a comprehensive GitLab CI/CD tutorial for building and deploying multi-architecture Docker images to AWS ECR. The tutorial should be structured in phases, with clear validation criteria at each step. The goal is to produce a high-quality, self-contained document that guides users from setup to deployment.

Using 41-how-to-create-the-best-tutorial.md principles, this prompt will ensure a focused, efficient, and high-quality output with comprehensive process tracking.

## INITIAL SETUP: Process Documentation Creation

**Goal**: Establish tracking system for entire tutorial creation process
**Output**: `process.md` with complete task checklist

### Process.md Creation Protocol

Before starting any tutorial work, create `process.md` with the following structure:

```markdown
# GitLab Docker Pipeline Tutorial Creation Process

## Phase 1: Blueprint Creation
- [ ] Research GitLab CI/CD documentation
- [ ] Research AWS ECR documentation  
- [ ] Research Docker buildx documentation
- [ ] Extract 3 key concepts from each source
- [ ] Identify 2 common failure points from each source
- [ ] Note version requirements for all tools
- [ ] Create 6-section outline
- [ ] Validate outline against criteria checklist
- [ ] Phase 1 completion review

## Phase 2: Section-by-Section Creation
### Section 1: Prerequisites
- [ ] Write prerequisites content (300-600 words)
- [ ] Add 1-2 code blocks with language tags
- [ ] Include verification steps
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 1 quality gate review

### Section 2: Environment Setup  
- [ ] Write environment setup content (300-600 words)
- [ ] Add 1-2 code blocks with language tags
- [ ] Include verification steps
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 2 quality gate review
- [ ] Sections 1-2 state summary

### Section 3: Basic CI Pipeline
- [ ] Write basic CI pipeline content (300-600 words)
- [ ] Add 1-2 code blocks with language tags
- [ ] Include verification steps
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 3 quality gate review

### Section 4: Multi-Architecture Build
- [ ] Write multi-arch build content (300-600 words)
- [ ] Add 1-2 code blocks with language tags
- [ ] Include verification steps
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 4 quality gate review
- [ ] Sections 1-4 state summary

### Section 5: ECR Deployment
- [ ] Write ECR deployment content (300-600 words)
- [ ] Add 1-2 code blocks with language tags
- [ ] Include verification steps
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 5 quality gate review

### Section 6: Troubleshooting
- [ ] Write troubleshooting content (300-600 words)
- [ ] Add 5 distinct failure scenarios
- [ ] Include solutions for each scenario
- [ ] Add troubleshooting tip
- [ ] Self-validation checklist (8+ items)
- [ ] Section 6 quality gate review
- [ ] Complete sections 1-6 state summary

## Phase 3: Assembly & Final Validation
- [ ] Sequential merge of all sections
- [ ] Add transition sentences between sections
- [ ] Generate table of contents with anchor links
- [ ] Insert 2 cross-references per section
- [ ] Consistency pass for command syntax
- [ ] Consistency pass for file path formats
- [ ] Consistency pass for version numbers
- [ ] Consistency pass for terminology
- [ ] Verify all code blocks have language tags
- [ ] End-to-end validation checklist
- [ ] Final quality metrics review
- [ ] Tutorial functionality test

## Quality Assurance
- [ ] Tutorial completion time under 2 hours
- [ ] 100% command success rate verification
- [ ] 5 failure modes addressed in troubleshooting
- [ ] Self-sufficiency test (no external research needed)
- [ ] Final tutorial publication

## Success Metrics
- [ ] Total word count: 2000-3500 words
- [ ] Total code blocks: 8-12
- [ ] All steps have verification methods
- [ ] Logical learning progression verified
- [ ] Production-ready tutorial confirmed
```

---

## PHASE 1: Blueprint Creation

**Goal**: Validated tutorial structure
**Context Load**: Minimal (outline + research notes only)
**Process Tracking**: Update process.md checkboxes as tasks complete

### Execution Protocol

1. **Research Collection** (output to scratchpad.md):

   ```text
   For each source (GitLab CI docs, AWS ECR docs, Docker buildx):
   - Extract 3 key concepts
   - Identify 2 common failure points
   - Note 1 version requirement
   ```

   **Process Update**: Check off research tasks in process.md as completed

2. **Outline Generation**:
   Create exactly 6 sections with defined scope:
   - Prerequisites (3 items max)
   - Environment Setup (5 steps max)  
   - Basic CI Pipeline (6 steps max)
   - Multi-Architecture Build (4 steps max)
   - ECR Deployment (5 steps max)
   - Troubleshooting (5 scenarios)

### Built-in Validation

**Check outline against these criteria:**

```text
✓ Exactly 6 main sections present
✓ Each section has step count within limits
✓ Prerequisites are concrete and achievable
✓ Logical flow: setup → basic → advanced → deploy → troubleshoot
✓ No circular dependencies between sections
```

**Validation Result**: PASS (proceed to Phase 2) / REVISE (fix specific issues)
**Process Update**: Mark Phase 1 completion in process.md

---

## PHASE 2: Section-by-Section Creation

**Goal**: Complete tutorial sections
**Context Load**: One section at a time
**Processing**: Linear, no parallelization
**Process Tracking**: Update section-specific checklists in process.md

### Single Section Protocol

**For each section (1-6), complete this cycle:**

1. **Write Section Content**:
   - Target: 300-600 words
   - Include exactly 1-2 code blocks
   - Add 1 verification step per major configuration
   - Use active voice, direct commands
   **Process Update**: Check off content writing task

2. **Self-Validation Checklist**:

   ```text
   Content Quality:
   ✓ Word count 300-600 (estimate by paragraph count)
   ✓ Every command shows expected output format
   ✓ At least 1 code block with proper language tag
   ✓ Contains exactly 1 "why this matters" explanation
   ✓ No undefined technical terms

   Style Requirements:
   ✓ Starts with action verb (Configure, Create, Set, etc.)
   ✓ Uses "you will" not "we will" 
   ✓ Code blocks include file paths
   ✓ Each step has clear success criteria
   ✓ Includes exactly 1 troubleshooting tip
   ```

   **Process Update**: Check off validation items as they pass

3. **Quality Gate Decision**:
   - **8+ checkmarks**: Section approved, proceed to next
   - **6-7 checkmarks**: Revise specific failing items only
   - **<6 checkmarks**: Rewrite section completely
   **Process Update**: Mark section quality gate completion

### Context Management

**After sections 2, 4, and 6:**

```text
State Summary (output this exactly):
- Completed: Section X through Y
- Current word count: [estimate]
- Next objective: [specific next section]
- Issues encountered: [any recurring problems or NONE]
```

**Process Update**: Check off state summary tasks in process.md

**Memory Reset Protocol**: Focus only on next section requirements, previous sections are locked.

---

## PHASE 3: Assembly & Final Validation

**Goal**: Production-ready tutorial
**Context Load**: Full document review
**Process Tracking**: Complete assembly and validation checklists

### Assembly Process

1. **Sequential Merge**:
   - Combine sections 1-6 in order
   - Add transition sentence between sections (1 sentence max)
   - Generate table of contents with anchor links
   - Insert exactly 2 cross-references per section
   **Process Update**: Check off merge and formatting tasks

2. **Consistency Pass**:

   ```text
   Scan for these issues:
   ✓ Same command syntax throughout (bash vs sh)
   ✓ Consistent file path format (relative vs absolute)
   ✓ Version numbers match across all sections
   ✓ Terminology used consistently (container vs image)
   ✓ All code blocks specify language
   ```

   **Process Update**: Check off each consistency item

3. **End-to-End Validation**:

   ```text
   Final Quality Metrics:
   ✓ Total length: 2000-3500 words
   ✓ Contains 8-12 code blocks total
   ✓ Every major step has verification method
   ✓ Troubleshooting covers 5 distinct scenarios
   ✓ Reader can follow without external research
   ✓ All commands include expected outputs
   ```

   **Process Update**: Check off validation metrics

### Success Criteria

**PASS Requirements (all must be true):**

- Tutorial is self-contained and executable
- Every command produces predictable results
- Troubleshooting section addresses real failure modes
- Final pipeline successfully builds and deploys test image
- Content follows logical learning progression

**FAIL Protocol:**

- 1-2 metrics fail: Fix specific issues only
- 3+ metrics fail: Return to Phase 2 for problematic sections
- Fundamental structure issues: Restart with refined outline

**Process Update**: Mark final success criteria completion

---

## Process Tracking Guidelines

### Checkbox Management

- **Mark completed tasks immediately** after finishing each item
- **Use [x] for completed**, [ ] for pending, [-] for skipped/not applicable
- **Update state summaries** at designated checkpoints
- **Document any deviations** from the original plan in process.md

### Quality Assurance Integration

- **Each checkbox represents a quality gate** that must pass before proceeding
- **Failed quality gates require documentation** of the issue and resolution
- **Process.md serves as audit trail** for tutorial creation methodology

### Adaptive Process Management

```text
IF section takes longer than expected:
- Document time variance in process.md
- Adjust remaining time estimates
- Note lessons learned for future improvements

IF quality gates repeatedly fail:
- Document recurring issues in process.md
- Consider process refinement
- Flag for post-completion review
```

---

## Adaptive Responses

### Length Management

```text
IF word count > 3500: Create "Quick Start" summary at beginning
IF word count < 2000: Expand examples and explanations
ELSE: Proceed with current structure
```

### Complexity Overflow

```text
IF any section becomes too complex:
- Move advanced topics to "Advanced Tips" callouts
- Keep main flow focused on core functionality
- Provide links to official docs for deep-dives
```

### Technical Constraints

```text
IF version incompatibilities discovered:
- Specify exact version requirements in Prerequisites
- Provide alternative commands for different versions
- Test with most common version combinations
```

---

## Quality Assurance Framework

### Continuous Validation

Each phase includes immediate quality feedback:

- **Phase 1**: Structural soundness check
- **Phase 2**: Section-level content validation  
- **Phase 3**: End-to-end tutorial functionality

### Error Recovery

- **Minor issues**: Fix in place without restarting phase
- **Major issues**: Restart current phase with lessons learned
- **Critical failures**: Document failure mode and restart entire process

### Success Metrics

**Quantifiable Outcomes:**

- Tutorial completion time: Under 2 hours for target audience
- Command success rate: 100% when followed exactly
- Troubleshooting coverage: Addresses 5 most common failure modes
- Self-sufficiency: No external research required during execution

---

## Execution Summary

**Initial Setup**: Create process.md with complete task tracking (5 minutes)
**Phase 1**: Create validated 6-section outline (10 minutes)
**Phase 2**: Write and validate sections sequentially (60 minutes)  
**Phase 3**: Assemble and perform final validation (20 minutes)

**Total Estimated Time**: 95 minutes
**Primary Output**: `42-gitlab-docker.md`
**Supporting Files**: `scratchpad.md` for research notes, `process.md` for task tracking

This approach maximizes content quality while minimizing process overhead, provides clear success criteria at every step, maintains focus on the core objective, and ensures comprehensive tracking of all tutorial creation activities through process.md checkboxes.

