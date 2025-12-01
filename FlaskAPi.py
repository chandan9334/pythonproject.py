from flask import Flask

app = Flask(_name_)

@app.route("/")
def myresume():
    return """
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <title>MyResume</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
            }

            .container {
                width: 800px;
                margin: 50px auto;
                background-color: #fff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #888;
            }

            h1, h2, h3 {
                margin: 0;
                padding-bottom: 10px;
            }

            .section {
                margin-top: 20px;
            }

            .section p {
                margin: 5px 0;
            }

            .skills span {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                margin: 5px;
                border-radius: 5px;
            }

            .experience, .education, .projects {
                border-left: 3px solid #4CAF50;
                padding-left: 10px;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>MyResume</h1>

            <div class='section contact'>
                <h2>Contact</h2>
                <p>Email: example@email.com</p>
                <p>Phone: +1234567890</p>
                <p>Website: www.example.com</p>
            </div>

            <div class='section skills'>
                <h2>Skills</h2>
                <span>HTML</span>
                <span>CSS</span>
                <span>JavaScript</span>
                <span>Python</span>
                <span>Flask</span>
            </div>

            <div class='section experience'>
                <h2>Experience</h2>
                <h3>Software Developer at ABC Corp</h3>
                <p>Worked on web applications, developed front-end and back-end features.</p>
                
                <h3>Intern at XYZ Solutions</h3>
                <p>Assisted in software projects and testing tasks.</p>
            </div>

            <div class='section education'>
                <h2>Education</h2>
                <h3>Bachelor of Technology in Computer Science</h3>
                <p>University Name, 2018 - 2022</p>
                
                <h3>High School</h3>
                <p>School Name, 2016 - 2018</p>
            </div>

            <div class='section projects'>
                <h2>Projects</h2>
                <h3>Project 1</h3>
                <p>Simple web application to manage tasks and track progress.</p>

                <h3>Project 2</h3>
                <p>Portfolio website with interactive UI and responsive design.</p>
            </div>
        </div>
    </body>
    </html>
    """

if _name_ == "_main_":
    app.run(debug=True)
