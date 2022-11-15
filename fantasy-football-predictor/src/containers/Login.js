import React, {useState} from "react";
import ReactDOM from "react-dom";

// jsx code for the login form
function Login(){
// store and object with an error message and the name of the field
    const [errorMessages, setErrorMessages] = useState({});
// boolean value to indicate if the form is successfully submitted or not
    const [isSubmitted, setIsSubmitted] = useState(false);

// User Login info
//TODO: make it connect to db for user info
    const database = [
        {
            username: "dschmidt2129@gmail.com",
            password: "Warrior$2129"
        }
    ];

    const errors = {
        uname: "invalid username",
        pass: "invalid password"
    };

    const handleSubmit = (event) => {
        //Prevent page reload
        event.preventDefault();

        var { uname, pass } = document.forms[0];

        // Find user login info
        const userData = database.find((user) => user.username === uname.value);

        // compare user info
        if (userData) {
            if(userData.password!== pass.value){
                //invalid password
                setErrorMessages({name: "pass", message: errors.pass});
            }else{
                setIsSubmitted(true);
            }
        }else{
            //Username not found
            setErrorMessages({name: "uname", message: errors.uname});
        }
    };

// generate jsx code for error message
    const renderErrorMessage = (name) => 
        name === errorMessages.name && (
            <div className="error">{errorMessages.message}</div>
        );

    //jsx code for login form
    const renderForm = (
        <div className="form">
            <form onSubmit={handleSubmit}>
                <div classname="input-container">
                    <label>Username</label>
                    <input type="text" name="uname" required/>
                    {renderErrorMessage("uname")}
                </div>
                <div classname="input-container">
                    <label>Password</label>
                    <input type="password" name="pass" required/>
                    {renderErrorMessage("pass")}
                </div>
                <div className="button-container">
                    <input type="submit"/>
                </div>
            </form>
        </div>
    );
    return (
        <div className="login">
            <div className="login-form">
                <div className="title">Sign In</div>
                {isSubmitted ? <div>User is successfully logged in</div> : renderForm}
            </div>   
        </div>
    );
}

export default Login;