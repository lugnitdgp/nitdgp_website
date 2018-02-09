import React from "react";

import Section from "./Section";

var axios = require('axios');

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      tiles: []
    };
  }
  componentDidMount() {
    axios("http://172.16.20.3:8000/dashboard")
      .then((response) => {
        this.setState({
          isLoaded: true,
          tiles: response.data.results
        });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
  createPageContent() {
    const { tiles } = this.state;
    var num_rows = Math.ceil(tiles.length/3);
    this.rows = [];
    for (var i = 0; i < num_rows ;  i++) {
      this.rows.push(
        <div className="row big-row" key={i}>
          {tiles.map((tile, index) => {
            if (index >= 3*i && index < 3*(i+1)) {
              return <Section key={index} tiles={tile}/>;
            }
          })}
        </div>
      );
    }
  }
  render() {
    const { error, isLoaded } = this.state;
    if (error) {
      return (
        <div>
          <p>Error: {error.message}</p>
        </div>
      );
    } else if (!isLoaded) {
      return (
        <div className="all-tiles l0">
          <p>Loading...</p>
        </div>
      );
    } else {
      this.createPageContent();
      return (
        <div className="page-content-container l0">
          <div className="all-tiles">
          {this.rows.map((row, index) => {
            return row;
          })}
          </div>
        </div>
      );
    }
  }
}
