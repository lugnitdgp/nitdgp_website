import React from "react";

export default class Footer extends React.Component {
  render() {
    return (
      <footer className="page-footer center-on-small-only">
          <div className="container" id="footer-container">
              <div className="container-fluid" align="center">
                  <div className="row" style={{"backgroundColor": "#fff", "padding": "5px", "borderRadius": "10px"}}>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo1.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo2.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo3.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo4.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo5.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" style={{"paddingTop": "10%"}} src="/static/img/govlogo6.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo7.png"/></a>
                    </div>
                    <div className="container-fluid logo-container">
                      <a href="#!"><img id="footer-logos" src="/static/img/govlogo8.png"/></a>
                    </div>
                  </div>
                  <hr className="style4"/>
                  <div className="row quick-links-row">
                    <div className="container-fluid quick-links-container">
                      <a className="waves-effect waves-light" href="#!"><span>Holidays</span></a>
                    </div>
                    <div className="container-fluid quick-links-container">
                      <a href="#!"><span>Archives</span></a>
                    </div>
                    <div className="container-fluid quick-links-container">
                      <a href="#!"><span>Policies</span></a>
                    </div>
                    <div className="container-fluid quick-links-container">
                      <a href="#!"><span>Webteam</span></a>
                    </div>
                  </div>
              </div>
          </div>
          <div className="footer-copyright" id="footer-copyright" >
              <div className="row">
                <div className="container-fluid" >
                    <span className="copyright-txt" >Last updated: 1/12/18 12:12 PM </span>
                </div>
                <div className="container-fluid" >
                    <span className="copyright-txt">© 2018 Copyright: <a href="https://www.nitdgp.ac.in"> nitdgp.ac.in </a></span>
                </div>
                <div className="container-fluid" >
                    <span className="copyright-txt">Visitors Count: 12312 </span>
                </div>
              </div>
          </div>
      </footer>
    );
  }
}
