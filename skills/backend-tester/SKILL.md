---
name: backend-tester
description: A backend tester that analyzes logs and creates comprehensive test files
---

# Backend Tester Skill

## Overview
A backend tester validates server-side logic, APIs, databases, and system integrations. They ensure reliability, security, and performance of backend services through comprehensive functional and non-functional testing. Backend testers work with logs, metrics, error tracking, and write automated test suites.

## Core Competencies

### Testing Fundamentals
- **Test Design**: Unit, integration, system, and E2E testing
- **Test Case Development**: Positive, negative, edge cases
- **Test Documentation**: Clear test plans, requirements traceability
- **Bug Reporting**: Reproduction steps, severity classification
- **Regression Testing**: Automated suites to catch regressions
- **Smoke Testing**: Quick validation of critical paths
- **Test Automation Strategies**: When to automate, maintenance approach

### API Testing
- **REST API Validation**: Methods (GET, POST, PUT, DELETE, PATCH), status codes
- **GraphQL API Testing**: Query, mutation, subscription testing
- **Request/Response Verification**: Headers, body, schema validation
- **Status Codes**: 2xx (success), 3xx (redirect), 4xx (client error), 5xx (server error)
- **Error Handling**: Error messages, error codes, error recovery
- **Rate Limiting & Throttling**: Request limits, backoff strategies
- **API Versioning**: Multiple version support, deprecation
- **API Contract Testing**: Schema validation, breaking changes
- **API Authentication**: API keys, OAuth, JWT, mutual TLS
- **API Documentation**: Swagger/OpenAPI validation

### Tools & Frameworks
- **Python Testing**
  - [pytest](https://docs.pytest.org): Modern testing framework
  - [unittest](https://docs.python.org/3/library/unittest.html): Standard library
  - [pytest-mock](https://pytest-mock.readthedocs.io): Mocking library
  - [pytest-cov](https://pytest-cov.readthedocs.io): Coverage reporting
  - [parameterized](https://github.com/wolever/parameterized): Parameterized tests
  - [hypothesis](https://hypothesis.readthedocs.io): Property-based testing
  - [tox](https://tox.readthedocs.io): Test automation and environments
  - [responses](https://github.com/getsentry/responses): HTTP mocking

- **REST API Testing**
  - [Postman](https://www.postman.com): API testing and documentation
  - [Insomnia](https://insomnia.rest): REST client
  - [REST Assured](https://rest-assured.io): Java/Groovy HTTP testing
  - [httpx](https://www.python-httpx.org): Modern Python HTTP client
  - [requests](https://requests.readthedocs.io): Simple HTTP library
  - [curl](https://curl.se): Command-line HTTP tool

- **GraphQL Testing**
  - [Apollo GraphQL Testing](https://www.apollographql.com/docs/apollo-server/testing/): Apollo test tools
  - [GraphQL Playground](https://www.apollographql.com/docs/apollo-server/testing/graphql-playground/): Interactive testing
  - [GraphQL Inspector](https://graphql-inspector.com): Schema validation
  - [Altair GraphQL Client](https://altair.sirmuel.design): GraphQL client

- **Mocking & Stubbing**
  - [unittest.mock](https://docs.python.org/3/library/unittest.mock.html): Built-in Python mocking
  - [responses](https://github.com/getsentry/responses): HTTP request mocking
  - [WireMock](https://wiremock.org): API mocking service
  - [Mockoon](https://mockoon.com): Mock API server
  - [json-server](https://github.com/typicode/json-server): Fake REST API

### Database Testing
- **SQL Testing**: Query validation, data integrity, transactions
- **SQL Injection Prevention**: Parameterized queries, prepared statements
- **Data Integrity**: ACID properties, constraint validation
- **Transaction Testing**: Rollback, commit, isolation levels
- **Database Performance**: Query optimization, index usage
- **Schema Validation**: Table structure, constraints, relationships
- **Data Migration Testing**: Data transformation validation, rollback
- **Database Seeding**: Test data setup, fixtures, factories

### Tools for Database Testing
- **Database Clients**
  - [SQLAlchemy](https://www.sqlalchemy.org): Python ORM and query builder
  - [psycopg2](https://www.psycopg.org): PostgreSQL adapter
  - [mysql-connector](https://dev.mysql.com/doc/connector-python/): MySQL adapter
  - [sqlite3](https://docs.python.org/3/library/sqlite3.html): SQLite driver

- **Database Fixtures & Factories**
  - [pytest-factoryboy](https://pytest-factoryboy.readthedocs.io): Factory Boy integration
  - [Faker](https://faker.readthedocs.io): Generate fake data
  - [factory_boy](https://factoryboy.readthedocs.io): Test data generation

- **Database Mocking**
  - [sqlalchemy-utils](https://sqlalchemy-utils.readthedocs.io): Database utilities
  - [testcontainers](https://www.testcontainers.org): Docker containers for testing
  - [SQLite in-memory](https://sqlite.org/inmemorydb.html): Fast test database

### Performance & Load Testing
- **Load Testing**: JMeter, Gatling, Locust
- **Stress Testing**: Push system to limits
- **Endurance Testing**: Extended duration testing
- **Spike Testing**: Sudden traffic increases
- **Soak Testing**: Running under load for extended time
- **Bottleneck Identification**: Finding slow operations
- **Scalability Validation**: Can system scale?
- **Response Time Analysis**: Target response times
- **Throughput Analysis**: Requests per second

### Load Testing Tools
- **Python**
  - [Locust](https://locust.io): Python load testing framework
  - [pytest-benchmark](https://pytest-benchmark.readthedocs.io): Benchmark tests

- **JVM**
  - [JMeter](https://jmeter.apache.org): Load testing tool
  - [Gatling](https://gatling.io): Load testing framework

- **Cloud**
  - [LoadImpact](https://loadimpact.com): Cloud load testing
  - [BlazeMeter](https://www.blazemeter.com): Load testing platform

### Security Testing
- **Vulnerability Testing**
  - SQL injection detection
  - XSS (Cross-Site Scripting) prevention
  - CSRF (Cross-Site Request Forgery) protection
  - Broken authentication/authorization
  
- **Authentication & Authorization**
  - JWT token validation
  - OAuth 2.0 flows
  - Session management
  - Permission enforcement
  - Privilege escalation attempts

- **Data Protection**
  - Encryption (HTTPS, data at rest)
  - Password hashing (bcrypt, argon2)
  - Data exposure (sensitive fields)
  - GDPR/compliance requirements

- **API Security**
  - Rate limiting enforcement
  - Input validation
  - Output encoding
  - Error message leakage
  - Dependency vulnerability scanning

- **Security Tools**
  - [OWASP ZAP](https://www.zaproxy.org): Security scanning
  - [Burp Suite](https://portswigger.net/burp): Penetration testing
  - [Bandit](https://bandit.readthedocs.io): Python security linter
  - [Safety](https://safety.readthedocs.io): Dependency vulnerability checking
  - [Snyk](https://snyk.io): Vulnerability scanning

### Integration & System Testing
- **Microservice Communication**: Service-to-service testing
- **Third-Party API Integration**: External service testing
- **Message Queues**: Event streaming (RabbitMQ, Kafka)
- **Cache Systems**: Redis, Memcached testing
- **Database Integration**: Full database testing
- **Service Dependency Mapping**: Understanding service relationships
- **End-to-End Workflow Validation**: Complete user journeys
- **Data Consistency**: Across distributed systems

### Integration Testing Tools
- **Containers & Orchestration**
  - [Docker](https://www.docker.com): Containerize services
  - [Docker Compose](https://docs.docker.com/compose/): Multi-service setup
  - [testcontainers](https://www.testcontainers.org): Spin up services in tests
  - [Kubernetes](https://kubernetes.io): Production deployment testing

- **Message Queues**
  - [RabbitMQ](https://www.rabbitmq.com): Message broker
  - [Apache Kafka](https://kafka.apache.org): Event streaming
  - [Redis](https://redis.io): Cache and message queue

### Debugging & Log Analysis
- **Log File Analysis**
  - Understanding log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Pattern matching in logs
  - Stack trace interpretation
  - Exception root cause analysis
  - Log aggregation (ELK, Datadog, Splunk)

- **Server Error Investigation**
  - 5xx error analysis
  - Timeout investigation
  - Resource exhaustion (memory, CPU)
  - Deadlock detection
  - Connection pool issues

- **Profiling & Optimization**
  - CPU profiling
  - Memory profiling
  - Query optimization
  - Network optimization
  - Thread analysis

- **Debugging Tools**
  - [logging module](https://docs.python.org/3/library/logging.html): Python logging
  - [debugpy](https://github.com/microsoft/debugpy): Python debugger
  - [pdb](https://docs.python.org/3/library/pdb.html): Python debugger
  - [gdb](https://www.gnu.org/software/gdb/): C/C++ debugger
  - [Datadog](https://www.datadoghq.com): Monitoring and logging
  - [Splunk](https://www.splunk.com): Log analysis
  - [ELK Stack](https://www.elastic.co/elastic-stack/): Log aggregation

### Best Practices & Patterns

#### Test Structure
```python
# Arrange-Act-Assert Pattern
def test_user_creation():
    # Arrange: Set up test data
    user_data = {"name": "Alice", "email": "alice@example.com"}
    
    # Act: Execute the action
    response = create_user(user_data)
    
    # Assert: Verify the result
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"
```

#### Test Organization
- **Naming**: `test_<functionality>_<scenario>_<expected_result>`
- **Location**: `tests/` directory mirroring source structure
- **Grouping**: Group related tests in test classes
- **Fixtures**: Reusable test data and setup
- **Parametrization**: Run same test with different inputs

#### Mocking Strategy
- Mock external dependencies (APIs, databases)
- Test in isolation
- Use responses library for HTTP mocking
- Use pytest-mock for function mocking
- Keep mocks simple and focused

#### Coverage Goals
- Aim for 80%+ code coverage
- Focus on critical paths
- Don't chase 100% coverage
- Measure branch coverage, not just line coverage
- Use `pytest-cov` for reports

#### Performance Testing Practices
- Establish baseline performance
- Test under realistic load
- Monitor resource usage
- Identify bottlenecks early
- Use load testing tools regularly

#### Security Testing Practices
- Test authentication flows
- Verify authorization boundaries
- Check input validation
- Test error messages (no information leakage)
- Verify encryption in transit and at rest
- Run dependency scanning regularly

### Test Writing Patterns

#### Unit Test Example
```python
import pytest
from services.payment import PaymentService

@pytest.fixture
def payment_service(mocker):
    service = PaymentService()
    service.gateway = mocker.Mock()
    return service

def test_payment_success(payment_service):
    # Arrange
    payment_service.gateway.charge.return_value = {"status": "success"}
    
    # Act
    result = payment_service.process_payment(100.0, "card_123")
    
    # Assert
    assert result["status"] == "success"
    payment_service.gateway.charge.assert_called_once()
```

#### API Test Example
```python
import httpx
import pytest

@pytest.mark.asyncio
async def test_get_user_endpoint():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api.example.com/users/123")
    
    assert response.status_code == 200
    assert response.json()["id"] == 123
    assert "name" in response.json()
```

#### Database Test Example
```python
@pytest.fixture
def test_db(mocker):
    db = Database(":memory:")
    yield db
    db.close()

def test_user_query(test_db):
    # Setup
    test_db.create_tables()
    test_db.add_user({"name": "Alice", "email": "alice@example.com"})
    
    # Test
    user = test_db.get_user_by_email("alice@example.com")
    assert user.name == "Alice"
```

#### Load Test Example
```python
from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def get_users(self):
        self.client.get("/api/users")

class WebsiteUser(HttpLocust):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
```

## Key Deliverables
- Comprehensive test suite with high coverage
- API test documentation and Postman collections
- Database test scripts with seed data
- Performance test reports with benchmarks
- Security audit findings and remediation
- Integration test scenarios and results
- Load and stress test results
- Detailed test execution reports
- Log analysis findings and root causes

## Metrics & Success
- **Coverage**: ≥80% code coverage
- **API Coverage**: 100% of endpoints tested
- **Database Coverage**: All CRUD operations tested
- **Bug Detection Rate**: Early detection through testing
- **Performance Baseline**: Establish and maintain performance targets
- **Security Issues**: Zero critical vulnerabilities
- **Test Reliability**: ≥98% test pass rate
- **Performance**: Tests complete within acceptable time
- **Maintenance**: Clear, maintainable test code

## Resources & References

### Official Documentation
- [pytest Documentation](https://docs.pytest.org): Python testing framework
- [Python unittest](https://docs.python.org/3/library/unittest.html): Standard library
- [FastAPI Testing](https://fastapi.tiangolo.com/advanced/testing-events/): FastAPI test patterns

### Testing Best Practices
- [Google Testing Blog](https://testing.googleblog.com): Testing articles
- [Martin Fowler Testing](https://martinfowler.com/articles/testing-strategies.html): Test strategies
- [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html): Testing levels

### API Testing
- [Postman Learning](https://learning.postman.com): API testing guide
- [REST API Testing Best Practices](https://restfulapi.net/http-status-codes/): Status code guide
- [API Testing Guide](https://www.softwaretestinghelp.com/api-testing/): Comprehensive guide

### Performance Testing
- [Locust Documentation](https://locust.io/docs.html): Load testing tool
- [JMeter Tutorials](https://jmeter.apache.org/usermanual/index.html): Performance testing
- [Performance Testing Guide](https://www.softwaretestinghelp.com/performance-testing-tutorial/): Best practices

### Security Testing
- [OWASP Top 10](https://owasp.org/www-project-top-ten/): Security vulnerabilities
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): Security testing
- [Bandit Security Linting](https://bandit.readthedocs.io): Python security

### Log Analysis
- [Python Logging](https://docs.python.org/3/library/logging.html): Logging guide
- [ELK Stack Guide](https://www.elastic.co/what-is/elk-stack): Log aggregation
- [Datadog Docs](https://docs.datadoghq.com): Monitoring and logging

### Database Testing
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org): ORM testing
- [Factory Boy Guide](https://factoryboy.readthedocs.io): Test data generation
- [Database Testing Best Practices](https://www.oracle.com/database/technologies/appdev/sqldeveloper/database-testing-best-practices.html)

## Quick Start for Backend Testing

1. **Setup Test Structure**: Organize tests in `tests/` directory
2. **Choose Framework**: Use pytest for Python projects
3. **Write Unit Tests**: Test individual functions/methods
4. **Create Fixtures**: Reusable test data and setup
5. **Mock Dependencies**: External APIs, databases, services
6. **Test APIs**: Validate endpoints, status codes, responses
7. **Database Tests**: Test queries, migrations, constraints
8. **Performance Tests**: Profile critical paths, load test
9. **Security Tests**: Validate auth, input validation, etc.
10. **Generate Reports**: Coverage, performance, security reports

---

**Last Updated**: March 24, 2026
**Status**: Enhanced with comprehensive tools, frameworks, and best practices
