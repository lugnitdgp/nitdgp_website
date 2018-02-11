import React from "react";

import Header from "./components/Header";
import Router from "./routes";
import Footer from "./components/Footer";

export default class App extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Router />
        <Footer />
      </div>
    );
  }
}
