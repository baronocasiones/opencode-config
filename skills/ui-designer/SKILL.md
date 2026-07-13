---
name: ui-designing
description: Create and/or analyze modern and responsive ui designs
---

# UI Designer Skill

## Overview
A skilled UI designer creates intuitive, visually appealing user interfaces that balance aesthetics with functionality. They translate user needs and business requirements into effective design solutions using modern design systems, accessibility best practices, and proven interaction patterns.

## Core Competencies

### Design Fundamentals
- **Color Theory**: Understanding color psychology, contrast, accessibility (WCAG AA/AAA standards)
- **Typography**: Font pairing strategies, hierarchy, readability at all viewport sizes
- **Layout Systems**: Grid-based design, flexbox principles, component-based layouts
- **Visual Hierarchy**: Emphasis through size, color, whitespace, and positioning
- **Spacing & Rhythm**: Consistent spacing scales (8px, 16px, 24px, 32px systems), visual balance
- **Composition**: Rule of thirds, golden ratio, visual weight distribution

### Modern Design System Principles
- **Atomic Design**: Atoms → Molecules → Organisms → Templates → Pages
- **Design Tokens**: Scalable, consistent values for colors, typography, spacing, shadows
- **Component Architecture**: Reusable, composable, well-documented components
- **Design System Maintenance**: Version control, change management, documentation
- **Design to Code Handoff**: Specs that developers can implement accurately

### Tools & Software
- **Figma**: Master prototyping tool, collaborative design, component libraries
- **Figma Features**: Design tokens, auto-layout, variants, plugins
- **Design System Documentation**: Living documentation (Storybook, Zeroheight)
- **Version Control**: Design file organization, naming conventions
- **Google Stitch**: Modern design framework, rapid prototyping

### User-Centered Design
- **User Research**: Personas, user flows, journey mapping
- **Wireframing**: Low-fidelity to high-fidelity progression
- **Mockups & Prototypes**: Interactive prototypes for usability testing
- **Usability Testing**: A/B testing, user feedback loops, iterative refinement
- **Accessibility (A11y)**: WCAG 2.1 AA/AAA compliance, color contrast ratios (4.5:1 text, 3:1 UI)
- **Inclusive Design**: Supporting assistive technologies (screen readers, keyboards)

### Interaction Design
- **Microinteractions**: Feedback, status, transitions, system communication
- **Animation Principles**: Easing, timing, purposeful motion (Disney's 12 principles)
- **Navigation Patterns**: Drawer, bottom tab, breadcrumb, tabs, pagination
- **Form Design**: Input validation, error messaging, progressive disclosure, field organization
- **State Management**: Hover, active, focus, disabled, loading, success, error states
- **Responsive Design**: Mobile-first approach, breakpoints (320px, 640px, 1024px, 1280px+)

### Visual Design Principles
- **Contrast**: Text/background (7:1 for WCAG AAA), color separation
- **Alignment**: Consistent grid alignment, visual logic
- **Consistency**: Repeated visual elements create coherence
- **Emphasis**: Draw attention to primary actions through size, color, position
- **White Space**: Breathing room, cognitive load reduction
- **Depth**: Elevation, shadows, z-index hierarchy

### Modern Design Patterns
- **Card-based Layouts**: Content containers with consistent structure
- **Modal Dialogs**: Focus management, keyboard accessibility, dismissal patterns
- **Floating Action Buttons (FAB)**: Primary action, accessibility considerations
- **Hamburger Menus**: Mobile navigation, accessibility labels
- **Infinite Scroll vs Pagination**: Use cases, performance, accessibility trade-offs
- **Search & Filter**: Autocomplete, tag chips, filter panels
- **Data Tables**: Column sorting, pagination, row selection, responsive behavior
- **Hero Sections**: Hero images, overlays, text contrast
- **Footer Design**: Information architecture, link organization

## Design System Reference Patterns

### Color Palettes (Non-Generic)
**Modern Approach**: Use meaningful color systems, not just default palettes
- **Primary Colors**: Brand identity (not default blue)
- **Semantic Colors**: Success (green), warning (amber), error (red), info (blue)
- **Neutral Scale**: Grays for backgrounds, text, borders (9-11 levels)
- **Accent Colors**: Supporting colors for emphasis
- **Accessibility**: Minimum 4.5:1 ratio for text, 3:1 for UI elements

**Example Color Systems**:
- Material Design 3: Tonal system based on primary color
- Tailwind: Curated color palette with multiple shades
- Semantic tokens: tie colors to meaning, not hex values

### Typography Systems (Non-Generic)
**Modern Approach**: Scalable type systems with clear hierarchy
- **Font Families**: Body (sans-serif), Headlines (distinctive), Monospace (code)
- **Font Sizes**: 12px, 14px, 16px (body), 20px, 24px, 32px, 48px (headings)
- **Line Heights**: 1.4-1.6 for body, 1.2 for headings
- **Font Weights**: Regular (400), Medium (500), Semibold (600), Bold (700)
- **Letter Spacing**: Tighter for headlines, normal for body

**Best Practices**:
- Limit to 2-3 font families maximum
- Use system fonts for performance (SF Pro, -apple-system, Segoe UI)
- Establish hierarchy ratios (1.125, 1.25, 1.333 modular scale)

### Spacing Systems (8px Grid)
- **Base**: 8px unit
- **Common Values**: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px
- **Usage**: Padding, margins, gaps, gutters follow the scale
- **Consistency**: Improves alignment, rhythm, and code handoff

### Shadow & Elevation (Material Design Approach)
- **Elevation Levels**: 0, 1, 2, 4, 8, 12, 16, 24 (shadow depth)
- **Box Shadows**: Consistent shadow combinations
- **Use Cases**: Cards, modals, dropdowns, FABs
- **Subtle**: Avoid heavy shadows unless depth is critical

### Border Radius (Consistency)
- **Standard Values**: 0px, 4px, 8px, 12px, 16px, full (50%)
- **Shapes**: Rounded buttons, card corners, input fields
- **Accessibility**: Rounded corners don't impact a11y

### Component States (Comprehensive)
Every interactive component should have:
- **Default**: Normal state
- **Hover**: Mouse over (desktop only)
- **Focus**: Keyboard focus (keyboard users, all devices)
- **Active**: Pressed/selected state
- **Disabled**: Non-interactive state
- **Loading**: Feedback during action
- **Success/Error**: Result states

## Interaction Design Patterns

### Button Variants
- **Primary**: Main actions (high emphasis)
- **Secondary**: Supporting actions (medium emphasis)
- **Tertiary**: Lowest emphasis, alternative actions
- **Danger**: Destructive actions (delete, remove)
- **Sizes**: Small, medium, large
- **States**: Default, hover, focus, active, disabled, loading

### Form Patterns
- **Text Inputs**: Placeholder, label, hint, error message
- **Validation**: Real-time, on-blur, on-submit
- **Error Messages**: Clear, specific, actionable
- **Password Fields**: Show/hide toggle
- **Select/Dropdown**: Native or custom with keyboard support
- **Checkboxes & Radio**: Clear label association, focus states
- **Switches**: Toggle state, animation feedback

### Modal Patterns
- **Focus Trap**: Keyboard focus stays within modal
- **Escape Key**: Dismiss on Escape (when appropriate)
- **Backdrop Click**: Optional dismissal (confirm dialogs shouldn't)
- **Scrollable Content**: Handle overflow gracefully
- **Animation**: Entrance/exit animation (optional)

### Navigation Patterns
- **Breadcrumbs**: Show location hierarchy
- **Tabs**: Switch between related content
- **Pagination**: Navigate large datasets
- **Infinite Scroll**: Load more content on scroll
- **Drawer/Sidebar**: Mobile navigation, collapsible
- **Bottom Navigation**: Mobile app tabs

## Modern Design Resources & References

### Design Principles & Systems
- [Material Design 3 (Google)](https://m3.material.io): Comprehensive design system with color, typography, spacing
- [Human Interface Guidelines (Apple)](https://developer.apple.com/design/human-interface-guidelines/): Platform-specific design patterns
- [Fluent Design System (Microsoft)](https://www.microsoft.com/design/fluent): Modern enterprise design
- [Ant Design (Enterprise)](https://ant.design): Component library + design principles
- [IBM Carbon](https://www.carbondesignsystem.com): Enterprise design system
- [Chakra UI](https://chakra-ui.com): Accessible component library + design tokens

### Color & Accessibility Tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): WCAG compliance validation
- [Coolers.co](https://coolors.co): Color palette generator
- [Color Hunt](https://colorhunt.co): Curated color palettes (not generic defaults)
- [Eva Design System Colors](https://colors.eva.design): Semantic color generation
- [Tailwind Color Palette](https://tailwindcss.com/docs/customizing-colors): Modern, accessible palette
- [Color Brewer](https://colorbrewer2.org): Scientific color schemes
- [Chroma.js](https://chroma.js.org): Advanced color manipulation

### Typography Resources
- [Font Pair](https://www.fontpair.co): Google Fonts pairing combinations
- [Typekit List](https://fonts.adobe.com): Premium fonts
- [Variable Fonts](https://fonts.google.com/?vfonly=true): Flexible, dynamic typography
- [Modular Scale](https://www.modularscale.com): Calculate harmonious type sizes
- [Font File Size Tool](https://www.fontsquirrel.com): Optimize font delivery
- [Grids & Guides](https://www.gridlover.net): Typography calculator

### Component & Pattern Libraries
- [Storybook](https://storybook.js.org): Component documentation and testing
- [Zeroheight](https://www.zeroheight.com): Design system documentation
- [Penpot](https://penpot.app): Open-source design tool (Figma alternative)
- [UI Patterns](https://www.uipatterns.com): Common interaction patterns
- [Mobbin](https://mobbin.com): Real app UI patterns and inspiration
- [Calltoidea](https://www.calltoidea.com): Design inspiration database
- [Awwwards](https://www.awwwards.com): Award-winning websites

### Figma-Specific Resources
- [Figma Design System Starter Kit](https://www.figma.com/community/file/903849862968484981): Ready-made design system
- [Figma Plugins](https://www.figma.com/community): Extend Figma capabilities
- [Design Tokens](https://www.figma.com/design-systems/tokens): Automated token generation
- [Figma Prototyping](https://help.figma.com/hc/en-us/articles/360040322773): Interactive prototypes
- [Figma Community Files](https://www.figma.com/community): Free design templates

### Accessibility (A11y) Standards
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/): Official accessibility standards
- [WebAIM Articles](https://webaim.org): Practical accessibility guides
- [Accessible Colors](https://accessible-colors.com): Check color contrast ratios
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/): Screen reader patterns
- [Inclusive Design](https://www.inclusivedesignprinciples.org): Design for everyone

### Interaction & Animation
- [Disney's 12 Principles of Animation](https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation): Timeless animation principles
- [Framer Motion](https://www.framer.com/motion/): React animation library
- [Lottie](https://lottiefiles.com): Complex animations library
- [Easings.net](https://easings.net): Easing function reference
- [Microinteractions](https://www.nngroup.com/articles/microinteractions/): Nielsen Norman article

### Design Inspiration (Non-Generic)
- [Dribbble](https://dribbble.com): Design community + portfolios
- [Behance](https://www.behance.net): Professional design showcase
- [Designer Hangout](https://www.designerhangout.co): Community discussions
- [The Outline](https://theoutline.com): Design-focused online magazine
- [It's Nice That](https://www.itsnicethat.com): Design and culture

### Performance & Optimization
- [Web Vitals](https://web.dev/vitals/): Google's performance metrics
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): Performance auditing
- [Image Optimization](https://web.dev/image-solutions/): Asset optimization
- [CSS-in-JS Performance](https://styled-components.com): Style delivery

### Responsive Design
- [Responsive Design Patterns](https://www.patterns.dev): Modern layout patterns
- [Tailwind CSS](https://tailwindcss.com): Utility-first framework with responsive design
- [CSS Grid & Flexbox](https://css-tricks.com): Modern layout techniques
- [Mobile-First Design](https://www.uxpin.com/studio/blog/mobile-first-design/): Design approach

## Key Deliverables
- High-fidelity design mockups in Figma
- Interactive prototypes with user flows
- Comprehensive design specification documents
- Design system documentation and component library
- Accessibility audit and WCAG compliance report
- Design handoff documentation for developers
- User testing findings and iterative improvements

## Metrics & Success
- Design consistency (100% token usage across designs)
- Accessibility compliance (WCAG AA/AAA standards met)
- Component reusability (% of design built from system components)
- Design handoff clarity (developer implementation accuracy)
- User satisfaction (usability testing scores)
- Performance impact (design file size, load time impact)
- A/B test results (visual design impact on conversions)

## Important Guidelines for Agent Usage

### Donts
- ❌ Don't create additional .md files to pollute the project directory
- ❌ Don't use generic, off-the-shelf color palettes (Tailwind defaults, Bootstrap blues)
- ❌ Don't use standard font stacks without consideration (Arial, Helvetica)
- ❌ Don't create designs that look like they came from template generators
- ❌ Don't ignore accessibility (WCAG compliance is non-negotiable)

### Dos
- ✅ Do use design tokens and systematic spacing
- ✅ Do create designs with distinctive, project-specific color palettes
- ✅ Do consider typography as a brand element
- ✅ Do test designs for accessibility with real tools
- ✅ Do build designs from component systems
- ✅ Do maintain consistency across all screens

### Notes
- Keep Stitch .md documentation minimal (max 5 files total if creating docs)
- Always refer to design system guidelines when creating new components
- Use Figma's component and token features for scalability
- Export designs with clear naming and organization for handoff

## Quick Start for Designers

1. **Start with Design System**: Check if one exists; if not, create one
2. **Define Color Palette**: 1 primary, semantic colors (success/warning/error), neutral scale
3. **Choose Typography**: 2-3 font families max, establish size/weight hierarchy
4. **Create Grid System**: 8px base unit, consistent spacing scale
5. **Build Components**: Create reusable components with all states
6. **Test Accessibility**: Run through WebAIM and contrast checkers
7. **Create Mockups**: Use components to rapidly build screens
8. **Prototype Interactions**: Show user flows and interactions
9. **Document Everything**: Leave clear specs for developers
10. **Iterate**: Gather feedback and refine

## Additional Resources

### Free Design Tools
- [Figma Free Tier](https://www.figma.com): Completely free for single projects
- [Penpot](https://penpot.app): Open-source Figma alternative
- [Excalidraw](https://excalidraw.com): Quick wireframing tool

### Learning Resources
- [Google Design Course](https://design.google/library/): Free design courses
- [Interaction Design Foundation](https://www.interaction-design.org): Free UX/UI courses
- [Design Observer](https://designobserver.com): Design critique and discussion

---

**Last Updated**: March 24, 2026
**Status**: Enhanced with comprehensive resources and modern design patterns
