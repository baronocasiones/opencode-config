---
name: ui-analyzer
description: Analyze ui from images and/or project descriptions to create comprehensive design specifications
---

# UI Analyzer Skill

## Purpose
Analyze user interface designs from images, screenshots, and project descriptions to generate comprehensive, structured design specifications. These specifications serve as the single source of truth for design implementation, ensuring consistency, accessibility, and developer-friendly documentation.

## Input Methods

### Images & Screenshots
- Screenshots of existing applications (mobile or web)
- Wireframes and low-fidelity mockups
- High-fidelity design mockups from Figma, XD, Sketch
- Design system screenshots and component libraries
- Competitor product screenshots for reference
- Functional prototypes or live applications

### Project Descriptions
- Product requirements and goals
- User personas and journey descriptions
- Brand guidelines and voice/tone
- Target audience and accessibility requirements
- Performance and technical constraints
- Competitive positioning and differentiation

### Combination Approach
- Images + descriptions provide complete context
- Images show "what", descriptions explain "why"
- Together they inform design decisions and trade-offs

## Output: Design Specification Document

A single, comprehensive `.md` file containing:
- **Design Overview**: Purpose, goals, target users
- **Color Palette**: Complete color system with semantic meaning
- **Typography**: Font families, sizes, weights, hierarchy
- **Spacing & Layout**: Grid system, spacing scale, layout patterns
- **Components**: All UI components with variants and states
- **Interaction Patterns**: Behaviors, animations, user feedback
- **Responsive Behavior**: Breakpoints, layout adaptations
- **Accessibility**: WCAG compliance, a11y considerations
- **Asset Requirements**: Images, icons, other resources
- **Design Tokens**: Technical tokens for implementation

## Analysis Process

### Phase 1: Visual Discovery
1. **Analyze Color Usage**
   - Primary, secondary, accent colors
   - Neutral scale (backgrounds, text, borders)
   - Semantic colors (success, warning, error, info)
   - Color contrast ratios (4.5:1 text, 3:1 UI)
   - Color psychology and brand alignment

2. **Extract Typography**
   - Font families and weights used
   - Heading sizes and hierarchy (H1-H6)
   - Body text size and line height
   - Monospace fonts for code
   - Font pairing analysis

3. **Identify Spacing & Layout**
   - Spacing scale (is it based on 4px, 8px, or custom?)
   - Padding and margin patterns
   - Grid layout system (columns, rows, gutters)
   - Alignment and distribution
   - Whitespace and breathing room

4. **Component Recognition**
   - UI components and their variants
   - Component states (default, hover, focus, disabled, etc.)
   - Component composition (what's made of what)
   - Reusable patterns and patterns

5. **Interaction Analysis**
   - Click/tap targets and hit areas
   - Hover states (desktop)
   - Focus states (keyboard navigation)
   - Animation and transition effects
   - Loading states and feedback

6. **Responsive Analysis**
   - Breakpoints (mobile, tablet, desktop)
   - Layout changes at each breakpoint
   - Mobile-first or desktop-first approach
   - Touch-friendly spacing and targets

### Phase 2: Requirements Extraction
1. **User Needs**
   - Who are the primary users?
   - What problems does the design solve?
   - What user journeys are supported?

2. **Business Goals**
   - What are the success metrics?
   - What conversions or behaviors are desired?
   - What sets this apart from competitors?

3. **Technical Constraints**
   - Performance requirements
   - Browser/device support
   - Implementation framework (React, Vue, etc.)
   - Animation/complexity limitations

4. **Accessibility Requirements**
   - WCAG target level (A, AA, AAA)
   - Keyboard navigation support
   - Screen reader compatibility
   - Color contrast standards
   - Assistive technology support

### Phase 3: Design Token Extraction
1. **Color Tokens**
   - Brand colors with semantic names
   - Neutral color scale
   - Semantic colors (success, error, warning, info)
   - Surface/background colors
   - Text/foreground colors

2. **Typography Tokens**
   - Font families
   - Font sizes (scale: 12, 14, 16, 20, 24, 32, 48)
   - Font weights
   - Line heights
   - Letter spacing

3. **Spacing Tokens**
   - Base unit (4px, 8px, etc.)
   - Spacing scale values
   - Common padding/margin values
   - Gap values for flex/grid

4. **Component Tokens**
   - Border radius values
   - Shadow definitions
   - Z-index layers
   - Transition/animation durations
   - Elevation levels

### Phase 4: Documentation Compilation
1. **Organize by Section**
   - Overview and context
   - Design tokens and system
   - Component library
   - Patterns and layouts
   - Accessibility guidelines
   - Implementation notes

2. **Provide Visual References**
   - Color swatches with hex codes
   - Typography specimens
   - Component diagrams
   - Layout grid visualization

3. **Include Code Examples**
   - CSS classes/variables for design tokens
   - Component prop examples
   - Responsive breakpoint code
   - Accessibility code snippets

4. **Create Developer-Friendly Output**
   - Consistent terminology
   - Clear hierarchy and navigation
   - Copy-paste ready code
   - Links to resources and tools

## Output Format & Structure

### File Organization
Single markdown file with clear sections:
- **Table of Contents**: Easy navigation to all sections
- **Design Overview**: Purpose, goals, users, constraints
- **Brand & Identity**: Logo, brand colors, voice/tone
- **Color System**: Complete color palette with tokens
- **Typography**: Font system with scale and usage
- **Spacing & Grid**: Layout system and spacing scale
- **Components**: Detailed component specifications
- **Patterns**: Reusable interaction patterns
- **Responsive Design**: Breakpoints and adaptations
- **Accessibility**: WCAG compliance and standards
- **Assets**: Image, icon, and resource inventory
- **Tokens**: Technical tokens for code generation
- **Implementation Notes**: Developer handoff info

### Visual Presentation
- **Color Swatches**: Hex codes, semantic names, usage
- **Typography Specimens**: Show each style in context
- **Component Diagrams**: States, variants, spacing
- **Layout Diagrams**: Grid, spacing, alignment
- **Code Blocks**: HTML, CSS, React examples
- **Tables**: Token values, breakpoints, specifications

## Core Competencies

### Visual Analysis
- **Color Perception**: Identify actual colors, harmony, contrast ratios
- **Typography Assessment**: Recognize font families, sizes, hierarchies
- **Layout Analysis**: Understand grid systems, spacing, structure
- **Component Identification**: Recognize UI patterns and their variations
- **Consistency Detection**: Spot patterns and recurring elements
- **Accessibility Analysis**: Evaluate contrast, focus states, keyboard navigation

### Design System Knowledge
- **Token-Based Design**: Understanding design tokens and their use
- **Component Architecture**: Atoms, molecules, organisms approach
- **Variant Design**: Component states and variations
- **Responsive Design**: Mobile-first, breakpoint strategy
- **Design Documentation**: Creating reusable specifications

### Technical Understanding
- **Web Standards**: HTML, CSS, responsive design
- **Development Frameworks**: React, Vue, Angular patterns
- **Accessibility Standards**: WCAG 2.1, ARIA
- **Performance Impact**: Design decisions affecting performance
- **Asset Optimization**: Image formats, icon systems

### Communication
- **Clear Documentation**: Writing specifications developers understand
- **Visual Documentation**: Diagrams, examples, visual hierarchy
- **Terminology**: Using consistent, technical language
- **Completeness**: Documenting all details without ambiguity
- **Organization**: Logical structure, easy navigation

## Key Resources & References

### Design System Documentation
- [Material Design 3 Specifications](https://m3.material.io): Complete design system with color, typography, spacing
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): Platform-specific patterns
- [Chakra UI Design Tokens](https://chakra-ui.com/docs/styled-system/customize-theme): Reference token structure
- [Design Tokens Format (DTCG)](https://tokens.designtokens.org): Industry standard token format

### Color & Contrast Analysis
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): WCAG contrast validation
- [Coolors Contrast Checker](https://coolors.co/contrast-checker): Visual contrast testing
- [Color Brewer](https://colorbrewer2.org): Semantic color analysis
- [Eva Design System Colors](https://colors.eva.design): Color generation with semantics
- [HSL Color Picker](https://www.htmlcolorcodes.com/hsl-color-picker/): Understand color relationships

### Typography Analysis
- [Type Scale Calculator](https://www.modularscale.com): Analyze font size relationships
- [Font Pairing Guide](https://www.fontpair.co): Understand typography combinations
- [Google Fonts Specimens](https://fonts.google.com): Reference typography
- [Grids & Guides](https://www.gridlover.net): Typography metrics calculator
- [Variable Fonts](https://fonts.google.com/?vfonly=true): Modern typography approach

### Component & Pattern Documentation
- [Material Design Components](https://m3.material.io/components): Standard component reference
- [Ant Design Documentation](https://ant.design): Enterprise component library
- [Storybook Documentation](https://storybook.js.org): Component documentation format
- [UI Patterns](https://www.uipatterns.com): Common patterns and examples
- [Mobbin](https://mobbin.com): Real app pattern analysis

### Spacing & Layout
- [Every Layout](https://every-layout.dev): Layout pattern reference
- [8pt Grid System](https://spec.fm/specifics/8-pt-grid): Spacing standardization
- [CSS Tricks - Grid](https://css-tricks.com/snippets/css/complete-guide-grid/): Grid system reference
- [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/): Responsive layout

### Accessibility & Inclusive Design
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/): Accessibility standards
- [Inclusive Design Principles](https://www.inclusivedesignprinciples.org): Design for everyone
- [WebAIM Articles](https://webaim.org): Practical accessibility guides
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/): Screen reader patterns
- [Color Accessibility](https://accessible-colors.com): Verify accessible colors

### Tools for Analysis
- [Figma](https://www.figma.com): Design inspection, design system review
- [Adobe Color](https://color.adobe.com): Color analysis and harmony
- [Contrast Ratio](https://www.contrastratios.com): Quick contrast checking
- [Responsively App](https://responsively.app): Responsive design testing
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/): Inspect designs in browser

### Documentation & Specification Writing
- [Design System Handbook](https://www.designsystems.com): How to document systems
- [Zeroheight](https://www.zeroheight.com): Design documentation platform
- [Component Pattern Documentation](https://atomicdesign.bradfrost.com): Atomic design approach
- [API Documentation Best Practices](https://spec.apisyouwonthate.com): Clear specification writing
- [Google's Design Documentation Guide](https://design.google/library/design-systems-101/): System documentation

## Analysis Workflow

### Step 1: Initial Review
- Review all provided images and descriptions
- Understand the project context and goals
- Identify design patterns and system

### Step 2: Color Analysis
- Extract all colors used
- Determine primary, secondary, accent, semantic colors
- Check contrast ratios for accessibility
- Assign meaningful token names

### Step 3: Typography Analysis
- Identify all font families and sizes
- Map type hierarchy and scale
- Note special treatments (weights, styles, spacing)
- Create font system definition

### Step 4: Layout & Spacing
- Identify spacing scale and base unit
- Map layout grid system
- Document padding, margins, gaps
- Establish responsive breakpoints

### Step 5: Component Identification
- List all unique components
- Document component variants and states
- Note special interactions or behaviors
- Show component hierarchy and composition

### Step 6: Interaction Patterns
- Identify hover, focus, active states
- Document animations and transitions
- Note loading and error states
- Map user interactions and feedback

### Step 7: Accessibility Audit
- Verify color contrast ratios
- Check focus state visibility
- Note keyboard navigation requirements
- Identify accessibility patterns used

### Step 8: Documentation
- Organize all findings into structure
- Create visual examples and diagrams
- Write implementation notes
- Package as single specification file

## Output Checklist

Before finalizing the specification document, verify:

- ✅ **Color System**: All colors identified with hex codes and semantic names
- ✅ **Typography**: Complete font system with sizes, weights, line heights
- ✅ **Spacing**: Established spacing scale with all used values
- ✅ **Components**: All UI components documented with variants
- ✅ **States**: All component states (default, hover, focus, active, disabled, loading)
- ✅ **Responsive**: Breakpoints and layout changes documented
- ✅ **Accessibility**: WCAG compliance verified, a11y patterns noted
- ✅ **Interactions**: All user interactions and animations documented
- ✅ **Tokens**: All design tokens organized and named
- ✅ **Developer Ready**: Documentation clear enough for implementation
- ✅ **Complete**: No ambiguities or missing information
- ✅ **Organized**: Table of contents, clear sections, easy navigation

## Key Deliverables
- Comprehensive design specification markdown file
- Color palette with contrast validation
- Typography system definition
- Spacing and layout grid documentation
- Complete component library with all variants
- Responsive design breakpoints and rules
- Accessibility compliance report
- Design tokens for implementation
- Developer handoff documentation

## Metrics & Success
- **Documentation Completeness**: 100% of design elements documented
- **Developer Implementation Accuracy**: 95%+ match to specification
- **Accessibility Compliance**: WCAG AA or AAA achieved
- **Component Reusability**: 90%+ of screens built from system components
- **Consistency Score**: 100% token usage across all documented designs
- **Handoff Clarity**: Zero clarification questions from developers

## Important Guidelines

### Donts
- ❌ Don't create vague descriptions; be specific with measurements
- ❌ Don't miss any design element; be comprehensive
- ❌ Don't use generic template language; make it project-specific
- ❌ Don't ignore accessibility; verify WCAG compliance
- ❌ Don't create multiple files; keep it in one specification document

### Dos
- ✅ Do use design tokens and systematic naming
- ✅ Do include color hex codes and semantic meanings
- ✅ Do verify all color contrast ratios
- ✅ Do document all component states
- ✅ Do create implementation-ready documentation
- ✅ Do use visual examples and code snippets
- ✅ Do organize logically with clear navigation

## Quick Start

1. **Review Input**: Understand project goals and constraints
2. **Color Analysis**: Extract and document color system
3. **Typography**: Map font system and hierarchy
4. **Components**: Identify and document all UI components
5. **States**: Document all component states and interactions
6. **Responsive**: Map breakpoints and responsive behavior
7. **A11y**: Verify accessibility and contrast
8. **Document**: Compile into specification file
9. **Validate**: Check completeness against checklist
10. **Deliver**: Provide single, comprehensive .md file

---

**Last Updated**: March 24, 2026
**Status**: Enhanced with comprehensive analysis methodology and resources
