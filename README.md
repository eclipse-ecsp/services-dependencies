[<img src="./images/logo.png" width="400" height="200"/>](./images/logo.png)

# services-dependencies
[![Maven Build & Sonar Analysis](https://github.com/eclipse-ecsp/services-dependencies/actions/workflows/maven-build.yml/badge.svg)](https://github.com/eclipse-ecsp/services-dependencies/actions/workflows/maven-build.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=eclipse-ecsp_services-dependencies&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=eclipse-ecsp_services-dependencies)
[![License Compliance](https://github.com/eclipse-ecsp/services-dependencies/actions/workflows/licence-compliance.yaml/badge.svg)](https://github.com/eclipse-ecsp/services-dependencies/actions/workflows/licence-compliance.yaml)
[![Latest Release](https://img.shields.io/github/v/release/eclipse-ecsp/services-dependencies?sort=semver)](https://github.com/eclipse-ecsp/services-dependencies/releases)

services-dependencies manages versions of Ignite and third-party dependencies.

## Table of Contents
* [Dependencies](#dependencies)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Built with Dependencies](#built-with-dependencies)
* [How to contribute](#how-to-contribute)
* [Code of Conduct](#code-of-conduct)
* [Authors](#authors)
* [Security Contact Information](#security-contact-information)
* [Support](#support)
* [Troubleshooting](#troubleshooting)
* [Licence](#license)
* [Announcements](#announcements)

## Dependencies
The following table lists the dependencies and their versions used in this project.

| Library name                     |   version   |
|----------------------------------|:-----------:|
| org.eclipse.ecsp:utils           | 1.1.0      |
| org.eclipse.ecsp:transformers    | 1.0.0      |
| org.eclipse.ecsp:nosql-dao       | 1.1.0      |
| org.eclipse.ecsp:sql-dao         | 1.1.2      |
| org.eclipse.ecsp:entities        | 1.1.1      |
| org.eclipse.ecsp:cache-enabler   | 1.0.0      |
| org.eclipse.ecsp:streambase      | 1.0.0      |
| org.mongodb:bson                 | 4.5.1      |
| org.mongodb:bson-record-codec    | 4.5.1      |
| org.mongodb:mongodb-driver-core  | 4.5.1      |
| org.mongodb:mongodb-driver-legacy | 4.5.1      |
| org.mongodb:mongodb-driver-reactivestreams | 4.5.1      |
| org.mongodb:mongodb-driver-sync  | 4.5.1      |
| org.yaml:snakeyaml               | 2.4        |
| joda-time:joda-time              | 2.14.0     |
| com.fasterxml.jackson:jackson-bom | 2.15.3     |
| com.hazelcast:hazelcast          | 5.5.0      |
| commons-io:commons-io            | 2.18.0     |
| com.google.protobuf:protobuf-bom | 4.30.2     |
| commons-lang:commons-lang        | 2.6        |
| org.apache.commons:commons-lang3 | 3.17.0     |
| de.flapdoodle.embed:de.flapdoodle.embed.mongo | 3.4.3      |
| com.github.kstyrc:embedded-redis | 0.6        |
| io.moquette:moquette-broker      | 0.17       |
| com.google.guava:guava           |  33.4.8-jre |
| com.101tec:zkclient              | 0.11       |
| org.apache.zookeeper:zookeeper   | 3.8.4      |
| de.siegmar:logback-gelf          | 6.1.1      |
| ch.qos.logback.contrib:logback-json-classic | 0.1.5      |
| ch.qos.logback.contrib:logback-jackson | 0.1.5      |
| org.json:json                    | 20240303   |
| com.bazaarvoice.jolt:jolt-core   | 0.1.8      |
| com.bazaarvoice.jolt:json-utils  | 0.1.8      |
| com.googlecode.json-simple:json-simple | 1.1.1      |
| org.wiremock:wiremock            | 3.12.1     |
| org.meanbean:meanbean            | 2.0.3      |
| org.jmockit:jmockit              | 1.24       |
| org.apache.commons:commons-compress | 1.26.2     |
| com.networknt:json-schema-validator | 1.0.86     |
| io.jsonwebtoken:jjwt             | 0.12.6     |
| com.nimbusds:nimbus-jose-jwt     | 10.2       |
| org.apache.kafka:kafka-clients   | 3.7.1      |
| org.apache.kafka:kafka-streams   | 3.7.1      |
| org.apache.kafka:kafka_2.13      | 3.7.1      |
| org.apache.kafka:connect-json    | 3.7.1      |
| org.apache.kafka:connect-api     | 3.7.1      |
| org.apache.kafka:kafka-raft      | 3.7.1      |
| org.apache.kafka:kafka-metadata  | 3.7.1      |
| org.apache.kafka:kafka-server-common | 3.7.1      |
| org.apache.kafka:kafka-storage   | 3.7.1      |
| org.apache.kafka:kafka-storage-api | 3.7.1      |
| com.auth0:jwks-rsa               | 0.22.1     |
| com.auth0:java-jwt               | 4.5.0      |
| org.projectlombok:lombok         | 1.18.38    |
| org.springframework:spring-framework-bom | 6.2.4      |
| org.springframework.boot:spring-boot-dependencies | 3.4.5      |
| org.springframework.boot:spring-boot-starter-validation | 3.4.5      |
| io.dropwizard.metrics:metrics-core | 4.2.30     |
| io.dropwizard.metrics:metrics-annotation | 4.2.30     |
| io.dropwizard.metrics:metrics-jvm | 4.2.30     |
| org.apache.httpcomponents.client5 :httpclient5 | 5.4.3      |
| org.apache.curator:curator-test  | 5.8.0      |
| org.hamcrest:hamcrest            | 3.0        |
| com.squareup.okhttp3:mockwebserver | 4.12.0     |
| org.testcontainers:testcontainers-bom | 1.21.0     |
| org.testcontainers:testcontainers | 1.21.0     |
| org.testcontainers:junit-jupiter | 1.21.0     |
| javax.activation:activation      | 1.1.1      |

## Getting Started

These instructions gets you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have the following:

* [Java jdk 17+](https://www.azul.com/downloads/?version=java-17-lts&package=jdk#zulu)
* [Maven 3.6 or higher](https://maven.apache.org/)

### Installation

A step-by-step series of examples that describe how to get a local development environment running.

Step 1: Build

```shell
$ mvn clean install
```

Step 2 : Add services-dependencies to API/SP Microservices as Parent

```xml
 <parent>
    <groupId>org.eclipse.ecsp</groupId>
    <artifactId>services-dependencies</artifactId>
    <version>1.0.XX</version> <!-- release version -->
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```

#### Coding style check configuration
[checkstyle.xml](./checkstyle.xml) is the HARMAN coding standard to follow while writing new/updating existing code.

Checkstyle plugin [maven-checkstyle-plugin:3.3.1](https://maven.apache.org/plugins/maven-checkstyle-plugin/) is integrated in [pom.xml](./pom.xml) which runs in the `validate` phase and `check` goal of the maven lifecycle and fails the build if there are any checkstyle errors in the project.

To run checkstyle plugin explicitly, run the following command:
```shell
mvn checkstyle:check
```

## Usage

Library Usage Document

Add services-dependencies to API/SP Microservices as Parent

```xml
<parent>
    <groupId>org.eclipse.ecsp</groupId>
    <artifactId>services-dependencies</artifactId>
    <version>1.0.XX</version> <!-- release version -->
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```

## Built With Dependencies

* [Spring Boot](https://spring.io/projects/spring-boot/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management

## How to contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details about contribution guidelines and the process for submitting pull requests to us.

## Code of Conduct

See [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for details about our code of conduct
and the process for submitting pull requests to us.

## Authors

* **Eugene Jiang** - *Initial work*
* **[Abhishek Kumar](https://github.com/abhishekkumar-harman)** - *Initial work*
* **Charles Zhu** - *Initial work*
* **Leon Chen** - *Initial work*

For a list contributors to this project, see the [list of [contributors](../../graphs/contributors).

## Security Contact Information

See [SECURITY.md](./SECURITY.md) to raise any security related issues.

## Support

Contact the project developers via the project's "dev" list - https://accounts.eclipse.org/mailing-list/ecsp-dev

## Troubleshooting

See[CONTRIBUTING.md](./CONTRIBUTING.md) for details about raising an issue and submitting a pull request to us.


## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](./LICENSE) file for details.


## Announcements

All updates to this library are documented in [releases](../../releases).
For the available versions, see the [tags on this repository](../../tags).
