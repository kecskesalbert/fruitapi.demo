The objective of this assignment is to assess your skills in developing a basic API and
your proficiency with version control, testing, and containerization.
In a real-world scenario we’d write this in either Python or Go, as those are the
programming languages we use on our team for real projects. For the purpose of this
assignment however, you are free to choose any programming language that you
are comfortable with.

Objective
Develop and package a simple Fruits API service with three endpoints, as described
below:
- Return all fruits in JSON format:
	[
		{
			"id": <ID>,
			"fruit": "apple",
			"color": "red"
		}
	]
- Return a specific fruit in JSON format.
- Add a fruit by sending a JSON payload.

Data Storage
Ensure that data is persistent across requests.

API Documentation
Your API should include clear instructions on how to interact with it, including how to
add a new fruit and retrieve fruits.

Requirements:
- Make the code available on GitHub or GitLab. Please provide a link to the
repository.
- Include tests to verify the functionality of your API.
- Create a CI/CD pipeline that performs the following steps:
	- Runs tests to ensure code integrity.
	- Builds a container image for your API.
	- Publishes the container image to the GitHub/GitLab container registry.

Submission
Once you have completed the task, please share the link to your repository and any
additional documentation necessary for us to review your project. Ensure that your
repository is well-structured and documented, making it easy for us to understand
and evaluate your work.
Our initial expectation is that you can complete the technical assignment within 2- 4
hours.
