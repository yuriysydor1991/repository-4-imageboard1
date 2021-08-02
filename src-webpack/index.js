import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js";
import AppLogin from "./AppLogin.js";
import AppPost from "./AppPost.js";

if (document.getElementById("root_home"))
	ReactDOM.render(<App />, document.getElementById("root_home"));

if (document.getElementById("root_login"))
	ReactDOM.render(<AppLogin />, document.getElementById("root_login"));

if (document.getElementById("root_post"))
	ReactDOM.render(<AppPost />, document.getElementById("root_post"));

