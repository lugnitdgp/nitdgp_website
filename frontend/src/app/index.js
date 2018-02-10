import React from "react";
import ReactDOM from "react-dom";

import "bootstrap";

import Home from "./components/Home";
import Header from "./components/Header";

const header = document.getElementById('header');
const pageContent = document.getElementsByClassName('page-content-container')[0];

ReactDOM.render(<Header/>, header);
ReactDOM.render(<Home/>, pageContent);
