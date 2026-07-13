---
name: frontend-tester
description: Frontend tester that can test UI, create automation scripts, and validate user interactions
---

# Frontend Tester Skill

## Overview
A frontend tester ensures web and mobile user interfaces function correctly, are responsive across devices, and provide a seamless user experience. They validate visual elements, interactions, performance from the user's perspective, and create automated test suites to catch regressions. Frontend testers work with browsers, emulators, and automation frameworks.

## Core Competencies

### Testing Fundamentals
- **Manual Testing**: Visual inspection, user interaction testing
- **Automated Testing**: Test scripts for regression prevention
- **Test Case Design**: Positive, negative, edge cases
- **Test Documentation**: Test plans, requirements traceability
- **Bug Reporting**: Screenshots, reproduction steps, severity
- **Regression Testing**: Automated suites to catch visual/functional changes
- **Smoke Testing**: Quick validation of critical user paths
- **Exploratory Testing**: Understanding features, finding edge cases

### Tools & Frameworks

#### Automation Frameworks
- **[Selenium WebDriver](https://www.selenium.dev)**: Cross-browser automation
  - Most mature and widely adopted
  - Supports all major browsers
  - Language support: Python, JavaScript, Java, C#
  - Learning curve: Medium to steep
  
- **[Cypress](https://docs.cypress.io)**: Modern end-to-end testing
  - Fast, developer-friendly
  - Real-time browser reload
  - Better debugging experience
  - JavaScript/TypeScript focused
  - Learning curve: Low
  
- **[Playwright](https://playwright.dev)**: Cross-browser automation
  - Fast and reliable
  - Modern API design
  - Multi-browser support (Chromium, Firefox, WebKit)
  - Language support: JavaScript, Python, Java, .NET
  - Learning curve: Low to Medium
  
- **[Puppeteer](https://pptr.dev)**: Headless Chrome automation
  - Fast, lightweight
  - JavaScript/Node.js focused
  - Good for automation and testing
  - Learning curve: Medium
  
- **[TestCafe](https://testcafe.io)**: Code-less and code-based testing
  - Simple API
  - No WebDriver required
  - Good cross-browser support
  - Learning curve: Low
  
- **[Nightwatch.js](https://nightwatchjs.org)**: WebDriver-based testing
  - Built on WebDriver protocol
  - JavaScript/Node.js focused
  - Good for continuous integration
  - Learning curve: Medium

#### Unit & Component Testing (React)
- **[Jest](https://jestjs.io)**: Zero-configuration testing framework
  - Snapshot testing
  - Code coverage
  - Great mocking capabilities
  - Most popular for React
  
- **[React Testing Library](https://testing-library.com/react)**: User-centric testing
  - Tests like a user would use the app
  - Encourages good testing practices
  - Complements Jest perfectly
  - Learning curve: Low
  
- **[Vitest](https://vitest.dev)**: Modern, fast test runner
  - Jest-compatible API
  - Vite integration
  - Faster than Jest
  - Great for modern stack
  
- **[Testing Playground](https://testing-playground.com)**: Debug testing queries
  - Interactive tool to learn queries
  - Test code generation
  
#### BDD & Specification Testing
- **[Cucumber](https://cucumber.io)**: BDD test automation
  - Gherkin language (human-readable)
  - Bridges QA and developers
  - Language agnostic
  
- **[Gherkin Syntax](https://cucumber.io/docs/gherkin/gherkin-reference/)**: Given-When-Then format
  - Clear test specifications
  - Non-technical readable tests

#### Visual Regression Testing
- **[Percy](https://percy.io)**: Visual testing service
  - Cloud-based visual regression
  - Intelligent diffing
  - Integration with CI/CD
  
- **[Chromatic](https://www.chromatic.com)**: UI testing and review
  - Component visual testing
  - UI review tool
  - Storybook integration
  
- **[BackstopJS](https://garris.github.io/BackstopJS/)**: Local visual regression
  - Automated screenshot comparison
  - Reference image management
  - Open source
  
- **[Pixelmatch](https://github.com/mapbox/pixelmatch)**: Pixel-level image comparison
  - Low-level image comparison
  - Customizable thresholds

#### Performance Testing
- **[Lighthouse](https://developers.google.com/web/tools/lighthouse)**: Performance auditing
  - Official Google tool
  - Measures Core Web Vitals
  - Accessibility and SEO scoring
  - Chrome DevTools integration
  
- **[WebPageTest](https://www.webpagetest.org)**: Detailed performance analysis
  - Real device testing
  - Waterfall charts
  - Network throttling simulation
  
- **[Puppeteer Performance](https://pptr.dev)**: Programmatic performance testing
  - Script performance metrics
  - Navigation timing API
  - CPU/memory profiling
  
- **[Speedcurve](https://www.speedcurve.com)**: Continuous performance monitoring
  - Production monitoring
  - Historical trends

#### Accessibility Testing
- **[axe DevTools](https://www.deque.com/axe/devtools/)**: Accessibility scanning
  - Free browser extension
  - WCAG 2.1 compliance checking
  - Integrates with test frameworks
  
- **[WAVE](https://wave.webaim.org)**: Web accessibility evaluation
  - Browser extension
  - Visual feedback on issues
  - Educational resources
  
- **[Lighthouse Accessibility](https://developers.google.com/web/tools/lighthouse)**: Built-in a11y testing
  - Part of Lighthouse audits
  - Automated checks
  
- **[jest-axe](https://github.com/nickcolley/jest-axe)**: Jest integration for axe
  - Automated a11y testing
  - Jest matcher for axe results
  
- **[Deque axe-core](https://github.com/dequelabs/axe-core)**: Accessibility engine
  - Core a11y testing library
  - Powers many tools

#### Browser & Device Testing
- **Cross-Browser Support**
  - Chrome, Firefox, Safari, Edge, IE
  - Mobile browsers (Chrome Mobile, Safari iOS)
  
- **Device Testing**
  - Physical device testing
  - Emulation (Android Studio, Xcode)
  - Cloud device labs (BrowserStack, Sauce Labs)
  
- **Device Labs**
  - **[BrowserStack](https://www.browserstack.com)**: Cloud browser/device testing
  - **[Sauce Labs](https://saucelabs.com)**: Cloud testing platform
  - **[LambdaTest](https://www.lambdatest.com)**: Cross-browser testing
  
- **Local Testing**
  - Chrome DevTools device emulation
  - Firefox responsive design mode
  - Safari responsive design mode

#### Browser DevTools
- **Chrome DevTools**
  - Inspector/Elements panel
  - Console for JavaScript errors
  - Network tab for API calls
  - Performance profiling
  - Memory profiling
  - Debugging (breakpoints, stepping)
  
- **Firefox Developer Edition**
  - Similar capabilities to Chrome
  - Grid and Flex visualization
  - CSS debugging
  
- **Safari Developer Tools**
  - Web Inspector
  - Network tab
  - Storage inspection

### Browser & Device Testing Skills

#### Cross-Browser Compatibility
- Testing on Chrome, Firefox, Safari, Edge
- Mobile browsers (iOS Safari, Chrome Mobile)
- Legacy browser support (if required)
- Feature detection vs. browser detection
- Graceful degradation strategies
- Progressive enhancement approach

#### Responsive Design Testing
- **Breakpoints**: Mobile (320px), Tablet (640px), Desktop (1024px), Large (1280px+)
- **Testing Strategy**: Mobile-first or desktop-first
- **Layout Changes**: Content adaptation at each breakpoint
- **Touch vs Click**: Different interaction models
- **Viewport Units**: vh, vw, vmin, vmax
- **Media Query Testing**: All breakpoints covered

#### Mobile-Specific Testing
- **iOS Testing**: iPhone/iPad, different screen sizes
- **Android Testing**: Various device brands, screen sizes
- **Touch Interactions**: Tap, long-press, swipe, pinch-zoom
- **Mobile Performance**: Battery, network, data usage
- **Mobile Forms**: Keyboard handling, input types
- **Mobile Navigation**: Bottom navigation, drawer menus

### Performance & Quality

#### Core Web Vitals Testing
- **Largest Contentful Paint (LCP)**: <2.5 seconds
- **First Input Delay (FID)**: <100 milliseconds
- **Cumulative Layout Shift (CLS)**: <0.1
- **First Contentful Paint (FCP)**: <1.8 seconds
- **Time to Interactive (TTI)**: <3.8 seconds

#### Performance Metrics
- **Load Time**: Time to fully load page
- **Time to First Byte (TTFB)**: Server response time
- **Rendering Performance**: Frame rate (60 FPS target)
- **Memory Usage**: Heap size, memory leaks
- **Network Requests**: Count, size, waterfall
- **JavaScript Execution**: Parse, compile, execution time
- **CSS Rendering**: Style recalculation, layout
- **Image Load Times**: Optimization, lazy loading

#### Performance Optimization Techniques
- **Code Splitting**: Load code on-demand
- **Image Optimization**: Compression, formats (WebP, AVIF)
- **Lazy Loading**: Defer non-critical resources
- **Caching**: Browser cache, service workers
- **Minification**: CSS, JavaScript, HTML
- **Compression**: GZIP, Brotli
- **CDN**: Content delivery network
- **Rendering Optimization**: Virtual scrolling, windowing

#### Memory Leak Detection
- Using Chrome DevTools Memory tab
- Heap snapshots for comparison
- Identifying detached DOM nodes
- Event listener cleanup
- Circular reference detection

#### Accessibility (A11y) Testing
- **Keyboard Navigation**: Tab order, focus visible
- **Screen Reader Testing**: NVDA, JAWS, VoiceOver
- **Color Contrast**: 4.5:1 for text, 3:1 for UI
- **ARIA Attributes**: Labels, roles, states
- **Focus Management**: Focus trap, focus restoration
- **Error Messages**: Clear, associated with fields
- **Form Labels**: Properly associated labels
- **Skip Links**: Navigation shortcuts
- **Alternative Text**: Image descriptions
- **WCAG 2.1 Compliance**: A, AA, or AAA level

### Debugging & Analysis

#### Browser Console Analysis
- JavaScript error messages
- Console warnings (deprecated APIs)
- Network errors (CORS, 4xx, 5xx)
- Performance warnings
- Security warnings (mixed content)

#### Network Analysis
- API request/response validation
- Status codes (200, 404, 500, etc.)
- Response headers and types
- Request payload verification
- Network waterfall analysis
- Slow request identification
- Failed request debugging

#### CSS & Layout Issues
- Layout shift detection
- Font loading performance
- CSS rendering bottlenecks
- Unused CSS identification
- Z-index stacking context
- Flexbox/Grid layout debugging

#### User Interaction Flow Analysis
- Click paths and conversions
- Form submission flows
- Navigation flows
- Modal and overlay handling
- Deep linking verification
- Back button behavior

### Automation Skills

#### Test Script Writing
- Selecting robust selectors (data-testid, aria-label)
- Waiting strategies (implicit, explicit, fluent)
- Page Object Model pattern
- Test data management
- Test state setup and teardown

#### Page Object Model Pattern
```javascript
// Page object encapsulates selectors and actions
class LoginPage {
  constructor(page) {
    this.page = page;
    this.usernameInput = 'input[name="username"]';
    this.passwordInput = 'input[name="password"]';
    this.loginButton = 'button[type="submit"]';
  }

  async login(username, password) {
    await this.page.fill(this.usernameInput, username);
    await this.page.fill(this.passwordInput, password);
    await this.page.click(this.loginButton);
  }
}
```

#### Test Data Management
- Fixtures for common test data
- Factories for complex objects
- Database seeding for test data
- API setup in test scripts
- Cleanup after test execution

#### Parallel Test Execution
- Running multiple tests concurrently
- Test isolation and state management
- Resource allocation
- Result aggregation
- Reporting from parallel runs

#### Flaky Test Identification & Fixes
- Timing issues (race conditions)
- Insufficient waits
- External dependencies
- Non-deterministic results
- Proper wait strategies

## Test Writing Patterns

### Unit Test Example (Jest + React Testing Library)
```javascript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Button from './Button';

describe('Button Component', () => {
  it('renders button with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('calls onClick handler when clicked', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    await userEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalled();
  });
});
```

### E2E Test Example (Playwright)
```javascript
import { test, expect } from '@playwright/test';

test('user can log in', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');
  await page.click('button[type="submit"]');
  
  await expect(page).toHaveURL('http://localhost:3000/dashboard');
  await expect(page.locator('text=Welcome')).toBeVisible();
});
```

### E2E Test Example (Cypress)
```javascript
describe('Login Flow', () => {
  it('should log in successfully', () => {
    cy.visit('/login');
    cy.get('input[name="email"]').type('user@example.com');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.contains('Welcome').should('be.visible');
  });
});
```

### BDD Test Example (Cucumber/Gherkin)
```gherkin
Feature: User Login
  Scenario: User logs in with valid credentials
    Given I am on the login page
    When I enter email "user@example.com"
    And I enter password "password123"
    And I click the login button
    Then I should see the dashboard
    And I should see "Welcome" message
```

### Accessibility Test Example (Jest + axe)
```javascript
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import MyComponent from './MyComponent';

expect.extend(toHaveNoViolations);

it('should not have accessibility violations', async () => {
  const { container } = render(<MyComponent />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

### Visual Regression Test Example (Playwright)
```javascript
test('button looks correct', async ({ page }) => {
  await page.goto('http://localhost:3000/components/button');
  await expect(page.locator('button')).toHaveScreenshot();
});
```

## Key Deliverables
- Automated test suite with high coverage
- Unit test files for components
- E2E test scenarios for user flows
- Accessibility test results (a11y audit)
- Performance reports (Lighthouse, WebPageTest)
- Visual regression test baseline and results
- Cross-browser compatibility matrix
- Mobile responsive test results
- Test execution reports and dashboards
- Bug reports with reproduction steps

## Metrics & Success
- **Unit Test Coverage**: ≥80% for components
- **E2E Coverage**: All critical user paths tested
- **Test Pass Rate**: ≥98% (flaky tests investigated)
- **Bug Detection**: Automated tests catch regressions
- **Performance**: Core Web Vitals targets met
- **Accessibility**: WCAG AA compliance achieved
- **Cross-Browser**: Support matrix verified
- **Mobile**: Responsive design validated
- **Test Speed**: Tests run in acceptable time

## Resources & References

### Official Documentation
- [Playwright Documentation](https://playwright.dev): Modern E2E testing
- [Cypress Documentation](https://docs.cypress.io): Developer-friendly E2E testing
- [Jest Documentation](https://jestjs.io): Unit testing framework
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/): React component testing

### Testing Best Practices
- [Testing Library Best Practices](https://testing-library.com/docs/queries/about): Query recommendations
- [Cypress Best Practices](https://docs.cypress.io/guides/references/best-practices): Cypress patterns
- [Testing React Components](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library): Common mistakes
- [E2E Testing Best Practices](https://www.cypress.io/blog/2018/12/20/my-best-practices-for-a-new-selenium-user/): Selenium/E2E patterns

### Performance Testing
- [Web Vitals Guide](https://web.dev/vitals/): Core metrics explanation
- [Lighthouse Documentation](https://developers.google.com/web/tools/lighthouse): Auditing tool
- [Performance Testing Guide](https://developer.mozilla.org/en-US/docs/Web/Performance): MDN performance guide

### Accessibility Testing
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/): Official standards
- [WebAIM Resources](https://webaim.org): Practical a11y guides
- [Accessible Colors](https://accessible-colors.com): Contrast checker
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/): Screen reader patterns

### Cross-Browser Testing
- [BrowserStack Documentation](https://www.browserstack.com/docs): Cloud testing
- [Sauce Labs Docs](https://docs.saucelabs.com): Cloud testing platform
- [MDN Browser Compatibility](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing): Cross-browser guide

### DevTools & Debugging
- [Chrome DevTools Guide](https://developer.chrome.com/docs/devtools/): Official guide
- [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/): Developer tools
- [Safari Web Inspector](https://developer.apple.com/safari/tools/): Safari tools

### Visual Regression
- [Percy Documentation](https://docs.percy.io): Visual testing service
- [BackstopJS Guide](https://garris.github.io/BackstopJS/): Visual regression tool
- [Chromatic Docs](https://www.chromatic.com/docs): Component testing

### BDD & Gherkin
- [Cucumber Documentation](https://cucumber.io/docs/): BDD framework
- [Gherkin Reference](https://cucumber.io/docs/gherkin/): Syntax guide
- [BDD Best Practices](https://cucumber.io/docs/bdd/): Writing good scenarios

## Quick Start for Frontend Testing

1. **Setup Test Framework**: Choose Jest + RTL for units, Playwright for E2E
2. **Write Unit Tests**: Component tests with RTL
3. **Create E2E Tests**: User flow scenarios
4. **Test Responsiveness**: Mobile, tablet, desktop breakpoints
5. **A11y Testing**: Run axe checks on components
6. **Performance Audit**: Run Lighthouse tests
7. **Cross-Browser**: Test on Chrome, Firefox, Safari
8. **Visual Regression**: Capture baseline screenshots
9. **Accessibility Audit**: WCAG compliance check
10. **Generate Reports**: Coverage, performance, accessibility dashboards

---

**Last Updated**: March 24, 2026
**Status**: Enhanced with comprehensive frameworks, tools, and best practices
