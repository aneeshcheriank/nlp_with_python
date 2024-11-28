# nlp_with_python
[![Python application test with GitHub Actions](https://github.com/aneeshcheriank/nlp_with_python/actions/workflows/makefile.yml/badge.svg)](https://github.com/aneeshcheriank/nlp_with_python/actions/workflows/makefile.yml)
## NLP project with python and fire
- extract text from wikipedia using python lib wikipedia
- extract noun phrases using lib text blob
- expose the function as a CLI using Fire

## Test fucntion
- mocking Web APIs with unitest.mock.patch
- coverage report for library
    - point --cov to the library root folder

## Additional readings

|Title|Type|Length(minutes)|Brief Description|
|---|---|---|---|---|
|[Create Functions](https://paiml.com/docs/home/books/minimal-python/chapter03-create-functions/)|Reading|30-60|Chapter 3 of this book focuses on creating functions in Python, emphasizing that functions are essential in modern Python programming, especially in cloud and machine learning contexts. Functions can be applied to diverse and complex problems with just a few lines of code. Examples discussed include functions with no input or return, functions that return without accepting input, and functions that accept input without returning. By understanding how functions work, beginners can unlock the potential of Python programming for various applications, such as Pandas DataFrames, AWS Lambda, or even creating web services. A well-designed function, which accepts input and returns some value, is crucial for building complex systems.|
|[Introduction to Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)|Reading|15-20|Azure Functions is a serverless solution that enables developers to focus on writing code while the cloud infrastructure handles deployment and maintenance. It provides compute resources on-demand to meet the fluctuating demands of applications, making it cost-effective and highly scalable. Azure Functions can be used for various scenarios such as web APIs, file processing, serverless workflows, database changes, scheduled tasks, message queue systems, IoT data streams, real-time data processing, and SQL database connections.<br><br> Developers can write functions in their preferred language, including C#, Java, JavaScript, PowerShell, or Python, and automate deployments with various tools and external pipelines. To troubleshoot, monitoring tools and testing strategies are available. Azure Functions offers flexible pricing options, such as the Consumption plan, which charges only for function runtime, and the Premium and App Service plans that cater to specific requirements.|
|[GitHub poject for Azure Functions in Rust](https://github.com/alfredodeza/rust-azure-function)|Reading|15-20|This repository provides a sample Rust application that can be deployed to Azure Functions using GitHub Actions, with Visual Studio Code recommended for development. The project demonstrates continuous deployment to Azure Functions with Rust, streamlining the development process. To get started, the following prerequisites are needed: an Azure account, Rust, Azure Functions Core Tools, Visual Studio Code, and the Azure Functions extension for Visual Studio Code. Additionally, the repository is Codespaces ready, allowing users to work directly from GitHub, only requiring an Azure account. For more information on Azure, refer to the Azure documentation.|
|[Developing Event-Driven Serverless](https://docs.google.com/presentation/d/1lAa88cZrYjrC1cnj-rwgiintsK9HO16R/edit#slide=id.p1)|Reading|15-20|This powerpoint presentation covers how AWS thinks about event driven services on AWS|
|[Python Fire CLI Framework](https://github.com/google/python-fire)|Reading|15-20|Python Fire is a versatile library that automatically generates command line interfaces (CLIs) from any Python object. It simplifies the creation of CLIs in Python, aids in developing and debugging code, and facilitates exploring and converting existing code into a CLI. Additionally, Python Fire eases the transition between Bash and Python and enhances Python REPL usage by preloading necessary modules and variables. As an action item, students are encouraged to explore the official examples to gain a deeper understanding of Python Fire's capabilities and potential applications.|

## Lesson reflections

- <b>Summary of Lesson</b> This lesson covered building Python functions from scratch, leveraging Python Fire to create CLIs, deploying serverless cloud functions, and using CI/CD to test Azure functions with GitHub Actions.

### Top 3 Key Points

- Python functions encapsulate reusable logic
- Python Fire auto-generates CLIs
- Cloud functions enable event-driven scale

### 5 Reflection Questions
- What types of logic lend themselves well to Python functions?
- How could Python Fire improve your existing scripts?
- What triggers might you use to execute serverless functions?
- Why build functions locally before cloud deployment?
- How does CI/CD apply for functions and microservices?

### 5 Challenge Exercises
- Package a script into a PyPi module with Python functions
- Refactor a script to add a Python Fire CLI
- Create functions responding to cloud events like S3 uploads
- Set up GitHub Actions testing for your Azure Functions
- Research best practices for breaking monoliths into functions
