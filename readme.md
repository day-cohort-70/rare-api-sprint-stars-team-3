# Rare Publishing README

Rare Publishing is a web application designed for writers and creators to publish, read, and discuss news and other content, primarily focused on technology and design. Built with React JS for the frontend and a Python and SQLite3 backend, Rare Publishing offers a platform for sharing ideas, insights, and innovations within these fields.

## Getting Started
### Prerequisites
Ensure you have Node.js and Python installed on your machine. 

### Backend Setup
1. Clone the server-side repository:

```
git clone https://github.com/day-cohort-70/rare-api-sprint-stars-team-3.git
cd rare-api-sprint-stars-team-3
```

2. Start the virtual environment

```
pipenv shell
```

3. Install dependencies:

```
pipenv install
```

4. Create a db.sqlite3 file:

```
touch db.sqlite3
```

5. Run the commands in the loaddata.sql file to create the tables in the database. In VSCode this can be achieved by highlighting the relevant lines, right-clicking, and selecting 'Run Selected Query'.

6. Start the server by clicking 'Start Debugging' within the 'Run and Debug' panel of VSCode or your chosen code editor/IDE.



### Frontend Setup

1. Clone the client-side repository:

```
git clone https://github.com/day-cohort-70/rare-client-sprint-stars-team-3.git
cd rare-client-sprint-stars-team-3
```

2. Install dependencies:

```
npm install
```

3. Start the development server:

```
npm start
```

### Running locally

To run the application locally, you need to have both the frontend and backend servers running simultaneously. Ensure the backend server is running, then start the frontend server. With both servers running, you can access the application through your browser at http://localhost:3000.

### Contributing

We welcome contributions from the community. Please feel free to submit pull requests or report issues.

### License

This project is licensed under the MIT License.

## Additional Resources

Frontend Repository: day-cohort-70/rare-client-sprint-stars-team-3
Backend Repository: day-cohort-70/rare-api-sprint-stars-team-3

## Contact

For inquiries or assistance, please reach out to our support team via email at support@rarepublishing.io.

## Acknowledgements

Thank you to all contributors who have helped shape Rare Publishing into what it is today. Your hard work and dedication are greatly appreciated.


