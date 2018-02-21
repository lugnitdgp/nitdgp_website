import React from "react";

export default class Carousel extends React.Component {
  render() {
    return (
      <div id="carousel-home" className="carousel slide carousel-fade" data-ride="carousel">
          <ol className="carousel-indicators">
            {this.props.slides.map((slide, index) => {
              return (
                <li data-target="#homepage-carousel" data-slide-to={index} className={index == 0 ? "active" : ""} key={index}></li>
              );
            })}
          </ol>
          <div className="carousel-inner" role="listbox">
            {this.props.slides.map((slide, index) => {
              return (
                <div className={["carousel-item", (index == 0 ? "active" : "")].join(' ')} key={index}>
                    <div className="view hm-black-light">
                        <img className="d-block w-100" src={slide.image} alt="First slide"/>
                        <div className="mask"></div>
                    </div>
                    <div className="carousel-caption">
                        <h3 className="h3-responsive">{slide.primary_caption}</h3>
                        <p>{slide.secondary_caption}</p>
                    </div>
                </div>
              );
            })}
          </div>
          <a className="carousel-control-prev" href="#homepage-carousel" role="button" data-slide="prev">
              <span className="carousel-control-prev-icon" aria-hidden="true"></span>
              <span className="sr-only">Previous</span>
          </a>
          <a className="carousel-control-next" href="#homepage-carousel" role="button" data-slide="next">
              <span className="carousel-control-next-icon" aria-hidden="true"></span>
              <span className="sr-only">Next</span>
          </a>
      </div>
    );
  }
}
