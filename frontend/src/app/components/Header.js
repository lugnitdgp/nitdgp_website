import React from "react";

export default class Header extends React.Component {
  render() {
    return (
      <div className="container-fluid">
        <nav className="navbar navbar-expand-lg navbar-dark darken-2" id="nav-below">
          <div className="container-fluid" >
                <div className="navbar-header">
                    <img className="navbar-brand" src="/static/img/nitdgp_logo_white.png" />
                    <img className="line-img" src="/static/img/line.png" />
                    <img className="navbar-img-small" src="/static/img/emblem.png" />
                    <div className="navbar-text white-text">
                      <div align="left">
                        <h6> National Institute of Technology Durgapur </h6>
                        <h6> राष्ट्रीय प्रौद्योगिकी संस्थान दुर्गापुर </h6>
                        <p className="navbar-text-small">(An Institute of National Importance under Government of <br/>India and Ministry of Human Resource Development)</p>
                      </div>
                    </div>
                    <img className="navbar-img-big" src="/static/img/emblem.png" />
                </div>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-4" aria-controls="navbarSupportedContent-4" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon" style={{"marginLeft": "-10px"}}></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarSupportedContent-4">
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item">
                            <a className="nav-link waves-effect waves-light navbar-link" href="#"><i className="fa fa-tasks"></i>Alumni</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link waves-effect waves-light navbar-link" href="#"><i className="fa fa-plane"></i>Webmail</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link waves-effect waves-light navbar-link" href="#"><i className="fa fa-address-book"></i>Contacts</a>
                        </li>
                    </ul>
                </div>
          </div>
        </nav>
        <nav className="mb-1 navbar fixed-top navbar-expand-sm" id="top-nav-wrap">
          <span align="left" className="top-nav-container-left">
            <a href="/" className="black-text"><i className="fa fa-home fa-lg" aria-hidden="true"></i></a>
          </span>
          <span align="right" className="top-nav-container-right">
              <a href="#" className="top-nav-link"> Old website </a>
              <a href="#" className="top-nav-link"> A+|A- </a>
              <a href="#" className="top-nav-link"> A|अ </a>
              <input id="search-btn-nav" type="text" name="" placeholder=" Search" />
          </span>
        </nav>
      </div>
    );
  }
}
