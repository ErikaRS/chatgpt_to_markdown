# Customer Reliability Engineering (CRE)

Created: 2024-03-29 14:40:12
Last Updated: 2024-03-29 14:40:50

### User - 2024-03-29 14:40:12

Just as SRE and DevOps professionalized making SaaS services reliable, is there a term for a similar effort focused on the reliability of systems that are meant to be deployed by the customer? In particular, what would the role of a DevOps like role focused on being able to have observability, reliability, scalability, debuggability, etc. of code in an environment to which the dev doesn't have direct access to be called? 

### Assistant - 2024-03-29 14:40:49

The concept you're describing—ensuring observability, reliability, scalability, and debuggability in customer-deployed environments—reflects an evolution and specialization within the broader fields of DevOps and Site Reliability Engineering (SRE). While DevOps and SRE practices have primarily focused on improving the reliability and performance of services managed by the service provider, there's a growing recognition of the need to extend these principles to customer-managed environments. This is particularly relevant for software and services deployed on-premises or in hybrid cloud environments where the provider does not have direct access or control.

The role and the practices you're describing don't have a universally recognized name yet, but they align closely with several emerging concepts and roles within the industry:

1. **Customer Reliability Engineering (CRE):** Borrowing from Google's CRE model, which extends SRE principles to help customers create and run reliable services, a similar approach can be applied to software deployed by customers. The focus here is on ensuring that both the software and the practices around its deployment and operation are designed to maximize reliability in environments outside the developer's direct control.

2. **Field Engineering or Solutions Engineering:** Often, professionals in these roles work closely with customers to deploy and optimize software solutions in a wide variety of environments. While traditionally more focused on the initial deployment and configuration, these roles are increasingly incorporating ongoing reliability and performance optimization into their scope.

3. **DevOps Consultant or Reliability Consultant:** These roles might involve working with a customer's internal teams to adopt practices and technologies that improve the reliability and observability of deployed solutions. This could include everything from infrastructure as code (IaC) to proactive monitoring and incident response planning.

4. **Enterprise DevOps:** A term that might emerge to specifically describe DevOps practices tailored to large, complex organizations, where software is often deployed across diverse and tightly-controlled environments. This would naturally include a focus on making these deployments as reliable and maintainable as possible, despite the lack of direct access by the software provider.

The core idea across these roles is to extend the principles of DevOps and SRE—such as automation, continuous integration/continuous deployment (CI/CD), monitoring, and incident management—to environments where the application is deployed by the customer. This involves creating robust documentation, offering tools for logging and monitoring that can be easily integrated into the customer's environment, and ensuring that the software is designed in a way that facilitates troubleshooting and scaling without direct vendor intervention.

While the industry has not settled on a single term for this role, the trend is clear: there's a growing need for professionals who specialize in making complex software systems reliable and manageable, even when those systems are running in environments outside of their direct control. This is an area likely to see significant growth and evolution in the coming years as more organizations look to balance the flexibility of customer-managed deployments with the reliability and performance standards they've come to expect from cloud-based services.

