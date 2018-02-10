import React from "react";
import ReactDOM from "react-dom";

import "bootstrap";

import Home from "./components/Home";
import Header from "./components/Header";
import Footer from "./components/Footer";

const header = document.getElementById('header');
const content = document.getElementById('content');
const footer = document.getElementById('footer');

ReactDOM.render(<Header/>, header);
ReactDOM.render(<Home/>, content);
ReactDOM.render(<Footer/>, footer);
