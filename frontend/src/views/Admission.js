import React from "react";
import $ from "jquery";
var axios = require('axios');

export default class Admission extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      admission: {},
      toggleState: {}
    };
  }
  componentDidMount() {
    axios("http://172.16.20.3:8000/academics/admission")
      .then((response) => {
        this.setState({
          isLoaded: true,
          admission: response.data.admission
        });
        var state = {};
        for (var degree in this.state.admission) {
          console.log(degree);
          state[degree] = 'OFF';
        }
        this.setState({
          toggleState: state
        });
        console.log(this.state.toggleState);
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
  createIdName(name) {
    return name.toLowerCase().replace(/\ /g, '-')
  }
  toggleView = (e, degree) => {
    var state = this.state.toggleState;
    console.log(degree);
    state[degree] = (this.state.toggleState[degree] == 'ON') ? 'OFF' : 'ON';
    this.setState({
      toggleState: state
    });
    console.log(this.state.toggleState);
  }
  render() {
    const { error, isLoaded, admission } = this.state;
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
      return (
        <div className="page-content-container l1">
          <div className="accordion" id="accordionEx" role="tablist" aria-multiselectable="true">
            {Object.keys(admission).map((degree, index) => {
              return (
                <div className="card" id={this.createIdName(degree)} key={index}>
                  <div className="card-header" role="tab" id={"heading"+index}>
                    <a data-toggle="collapse" data-parent="#accordionEx" href={"#collapse"+index} aria-expanded="false" aria-controls={"collapse"+index} onClick={(e) => this.toggleView(e, degree)}>
                      <h5 className="mb-0">{degree}<i className={this.state.toggleState[degree] == 'ON' ? "fa rotate-icon fa-angle-down" : "fa rotate-icon fa-angle-up"}></i></h5>
                    </a>
                  </div>
                  <div id={"collapse"+index} className="collapse" role="tabpanel" aria-labelledby={"heading"+index}>
                    <div className="card-body">
                      <div className="card-text">
                        <ul className={"contents"+index}>
                          {admission[degree].map((program, i) => {
                            return (
                              <li key={i}>
                                <h1>{Object.keys(program)[0]}</h1>
                                <ul className={this.createIdName(Object.keys(program)[0]) + '-' + i}>
                                  {program[Object.keys(program)].map((notice, j) => {
                                    return (
                                      <li key={j}><a href={notice.file}>{notice.title}</a></li>
                                    )
                                  })}
                                </ul>
                              </li>
                            )
                          })}
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      );
    }
  }
}
