import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "./views/Home";
import Calendar from "./views/Calendar";
import Admission from "./views/Admission";

export default class Router extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/academics/calendar" exact component={Calendar} />
          <Route path="/academics/admission" exact component={Admission} />
        </Switch>
      </BrowserRouter>
    );
  }
}


module.exports = Router;
