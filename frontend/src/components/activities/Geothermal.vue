<template>
  <div class="l3-fac">
    <sp-card containerclass="l3-card">
      <div slot="header">
        <p class="tile-title-text">
          <a class="white-text">
            GEOTHERMAL HELIUM EARTHQUAKE PRECURSOR
          </a>
          <span v-if="!general" @click="general = true">
            - Show
          </span>
        </p>
      </div>
      <div class="container-fluid fac-sm">
        <div class="row">
          <div class="list-group"
            :class="extraNavClasses.concat([getClassNav()])"
            :style="{ top: popUpTop + 'px' }">
            <a class="dropdown-item active"  data-toggle="list" href="#li1" role="tab">About Us</a>
            <a class="dropdown-item"  data-toggle="list" href="#li2" role="tab">Brief History</a>
            <a class="dropdown-item"  data-toggle="list" href="#li3" role="tab">Members</a>
            <a class="dropdown-item"  data-toggle="list" href="#li4" role="tab">Research Activities</a>
            <a class="dropdown-item" data-toggle="list" href="#li5" role="tab">Equipment</a>
            <a class="dropdown-item" data-toggle="list" href="#li6" role="tab">Field Visit Report</a>
            <a class="dropdown-item" data-toggle="list" href="#li8" role="tab">Publications</a>
            <a class="dropdown-item" data-toggle="list" href="#li7" role="tab">Seminar</a>
            <a class="dropdown-item" data-toggle="list" href="#li9" role="tab">Photo gallery</a>
            <a class="dropdown-item" data-toggle="list" href="#li10" role="tab">Contact Us</a>
          </div>
          <div class="downc tab-content" :class="getClassContent()">
            <button class="btn" type="button" @click="showNav($event)">
              <i class="fa fa-bars fa-2x"></i>
            </button>
            <div class="tab-pane fade show active big-list" id="li1" role="tabpanel">
              <h4 class="pane-title" align="center">About Us</h4>
              <hr>
              <p class="text-justify">
                The research focus of Center of Helium and Geothermal Research at NIT Durgapur is namely three fold
                <ul>
                  <li>harnessing helium gas from geothermal resources (hot springs)</li>
                  <li>exploration of geothermal power</li>
                  <li>monitoring of earthquake precursory signals.</li>
                </ul>
                Helium consumption in India is approximately 0.15 billion cubic feet, about 2.3% of global helium consumption, most of which is imported from USA. Poland and Qatar are among the countries that produce helium, but have till the date limited export capability. India is entirely dependent on USA for tapping helium. USA is already turning off helium supplies to the outside world. The immediate implication is the serious consequences on our space, defense and atomic energy programme along with a whole host of other areas such as MRI’s medical equipment that will plunge into despair and come to a grinding halt. The switch off also implies serious problems to our R&D programme in the Indian laboratories. In the light of this, we have far too long taken the Micawberish attitude that something will turn up to save the situation. However, no comprehensive effort has been undertaken so far to map and extract helium in the country in a large scale. It is essential therefore for India to seriously initiate its own programme to produce helium in a large scale, in order to be reasonably self-reliant. British geologist identified more than three hundred hot springs in India. Out of over 300 hot springs scattered throughout the country many release gases enriched with helium (concentration > 1.0 vol.% ). On the other hand all the known natural petroleum gas fields in India are lean in helium (0.05 vol.% in average). And to recover helium from natural petroleum gas, a host of allied factors need to be taken into account including the natural petroleum gas well life-time, before a helium extraction unit can be set-up. As an alternate measure, exploring helium extraction from geothermal areas appears promising because of higher helium concentrations (1.0 vol% in average in hot spring gases, 20 times higher than helium concentration in natural petroleum gases) available for virtually inexhaustible time-scale durations (geological time scale). It is always economical to recover helium from a gas source having high helium content with high flow rate.<br>
                These hot springs may also be utilized as a source of geothermal power - a vital source of energy (green energy) still completely ignored in India. The thermal energy of the solid earth originates from the primordial heat locked up within its interiors during the formation of the planet, along with subsequent heat generated during geologic time on account of the radioactive decay of the isotopes in the elements of Uranium and Thorium series. High temperature and pressure within the earth cause rocks to melt. This is known as magma. Because it is lighter than rock, magma rises up and heats the rocks above. This is a heat source. It is known as geothermal energy. Geothermal energy is more easily accessible in areas where there are hot springs.However, no comprehensive effort has been undertaken so far to map and harness geothermal energy in the country. It is thus essential and timely for India to seriously initiate its own programme to generate geothermal power in a large scale. Geothermal electricity is grid interactive and has no dependence on meteorological parameters unlike wind or solar energy. Geothermal resources can sustain for long time. The most important aspect is that environmental impact of the geothermal power plant is negligible. The geothermal zones of India have a moderate to high geothermal gradient (47-1000 C) and heat flux (78-468 mW/m2). There are vast regions in the country that are characterised with high geothermal gradient (> 600 C) and high heat flux (> 200 mW/m2) and these geothermal zones could well utilized for generation of green power.<br>
                In this context a three year R&D project has been taken up by NIT Durgapur for detailed investigation towards large scale extraction of helium and geothermal energy at the Bakreswar-Tantloi geothermal region lying across the border districts of Birbhum in West Bengal and Dumka in Jharkhand.Both the idea of “extraction of helium in large scale” and “geothermal power” at Bakreswar-Tantloi geothermal area is complementary to each other. Helium and geothermal heat is coupled to each other. Both of them are produced from common source of uranium and thorium, present in the crustal rock and also in mantle. Hot spring with sizeable helium content in the emanating natural gas should in principal lead to large natural heat source not too far away from the surface of the earth. This is a fact especially so if one compares the depth to which one has to drill in areas where there is no hot spring with escaping natural gas. Therefore, a common deep drilling (~300-800 m deep) at Bakreswar-Tantloi geothermal area could be used to tap both the helium sources and geothermal resources.<br>
                Apart from this, the center is also actively involved in research on monitoring of earthquake precursory signals through geochemical and geophysical techniques. So far four monitoring laboratories are operated by NIT Durgapur at different corners of the country. Themonitoring stations are placed in dissimilar geological environments and in different seismic zones of the country.The names and locations of the laboratories are as
                <ul>
                  <li>Thermal spring site at Bakreswar, Birbhum, West  Bengal</li>
                  <li>Thermal spring site at Tantloi, Dumka, Jharkhand</li>
                  <li>Thermal spring site at TattaPani, Rajouri, Jammu & Kashmir</li>
                  <li>The mud volcano at Baratangisland, Andaman & Nicobar islands</li>
                </ul>
                And the data analysis centre is situated at Dept. of Physics, NIT Durgapur, Durgapur, West Bengal Different kind of instruments such as gas chromatograph, radon monitor, seismometer etc. is installed at the said laboratories to collect the geochemical and geophysical data.The recorded data are sent to the data analysis centre through VSAT internet connectivity for further analysis.
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li2" role="tabpanel">
              <h4 class="pane-title" align="left">Brief History</h4>
              <hr>
              <p class="text-justify">
                Serious search for large-scale helium in India began during the first years of the 1970’s by the legendary S. N. Bose, FRS, National Professor of Physics. Professor Bose had the foresight to recognize that India would need substantial quantities of helium gas in future to feed its emergent requirements in crucial scientific areas. And this supply must essentially come out of its own natural resources. Accordingly, he started off a ‘Helium Recovery’ project at the Indian Association for the Cultivation of Science (IACS) at Jadavpur, Kolkata, during 1971. The entire task of planning and execution of this project was entrusted to the well-known experimental physicist, Professor S. D. Chatterjee, one of the distinguished students of Professor Bose. Prof. Chatterjee noted the presence of helium in the hot spring (72oC) gas emissions at Bakreswar, near Santiniketan, West Bengal. The helium content of the Bakreswar gas was about 1.8 volume percent. The helium recovery pilot plant (helium recovery from hot spring gas) built by Prof. Chatterjee and his colleagues at Bakreswar was a remarkable breakthrough. It immediately attracted the attention of Department of Science and Technology (DST) and Department of Atomic Energy (DAE). And therefore, in 1977 at the insistence of Dr. H. N. Sethna, the then Chairman, Atomic Energy Commission (AEC) along with Dr. A. S. Divatia, Project Manager, Variable Energy Cyclotron Centre (VECC), Kolkata the work concerning helium recovery done at IACS was transferred to VECC from March 1978. The related field work was taken charge of by the Atomic Mineral Directorate (AMD) of DAE. This part was also subsequently transferred to VECC in 1982. Around 1984, Prof. Bikash Sinha came to VECC from BARC and he got interested in the project, especially after meeting Professor S.D. Chatterjee who had extraordinarily original and innovative ideas and was greatly admired by Dr. Raja Ramanna and Prof. Sinha. Meanwhile, helium extraction from the nearby geothermal field at Tantloi (Jharkhand) also started through a joint venture of DST, VECC and Saha Institute of Nuclear Physics (SINP), Kolkata. A purification plant was installed improving recovered helium purity to 99.99 per cent purity level. In the year 2009 a prototype helium extraction plant was also installed at natural gas field at Kuthalam, Tamilnadu by VECC, SINP in collaboration with DST and Oil and Natural Gas Corporation (ONGC) to extract helium from natural gas having feeble helium concentration of 0.05 volume percent. It was demonstrated for the first time in the country that it is very much possible to recover helium from natural petroleum gases having feeble helium content (0.05 vol.%). Moreover that extreamly low concentration helium bearing natural petroleum gas was purified using Pressure Swing Adsorption (PSA) technique to produce a high grade helium (99.0 vol.% pure helium). The installation and commissioning of the PSA helium pilot plant (helium recovery from natural petroleum gas) along with purification unit (99.0 vol.% pure helium) was a remarkable breakthrough.  <br>
                Prof. Bikash Sinha in his capacity as Homi Bhabha Professor of DAE along with some young colleagues continued the programme, which was funded by Ministry of Earth Sciences (MoES). Prof. Bikash Sinha and his group performed geochemical and geophysical research activities at Bakreswar-Tantloi geothermal region, West Bengal and in Jharkhand. The work brought to light two vital conclusions:
              <ul>
                  <li>The entire Bakreswar-Tantloi geothermal area is sitting on a huge reservoir of helium existing within the crust not far beneath from the top soil. The surface expression of helium, as seen at hot spring bubble gas, figures only but a tiny fraction of this reservoir. This region hosts almost 60 hot springs within 2500 square km area. These hot springs are enriched with high concentration of helium (1.88-2.77 vol.%.). Indeed, this fact was surmised and mentioned long time ago by Professor S. D. Chatterjee to Prof. Bikash Sinha. We wish to explore the entire topology and the extent of the helium reservoir.</li>
                  <li>The high geothermal heat outflow (230 mW/m2), geothermal gradient (90 0C/km) is seen in this area. Also high concentration of helium and radon (radioactive gas) are emanating from the hot springs of this zone. These data indicates the presence of a potential geothermal resource in the area. This area will be ideal for setting up a “geothermal” energy reactor - a vital source of energy (green energy) still completely ignored in India.</li>
                </ul>
                Presently the entire programme is operated from NIT Durgapur. A high level scientific community is monitoring and supervising the said activity.
                <img src="https://old.nitdgp.ac.in/helium_geothermal/images/clip_image002_0000.jpg">
              </p>

            </div>

            <div class="tab-pane fade big-list" id="li3" role="tabpanel">
              <h4 class="pane-title" align="left">Members</h4>
              <hr>
              <p class="text-justify">
                <links-page>
                      <card title="Faculty and Scientists">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in faculties" :key="i" :name="person.name" :image="person.image">
                            {{person.designation}}<br><hr>
                            <strong>Status: </strong>{{ person.specility }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                    <links-page>
                      <card title="Advisor">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in advisors" :key="i" :name="person.name" :image="person.image">
                            {{person.designation}}<br><hr>
                            <strong>Status: </strong>{{ person.specility }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                    <links-page>
                      <card title="Technical staff members">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in members" :key="i" :name="person.name" :desig="person.designation" :image="person.image">
                            <strong>Location: </strong>{{ person.location }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
                    <br>
                  <links-page>
                      <card title="Research Students">
                        <div class="row">
                          <card-testimonial v-for="(person, i) in students" :key="i" :name="person.name" :image="person.image">
                            {{person.designation}}<br>
                            <strong>Email: </strong>{{ person.email }}<hr>
                            <strong>Tropic: </strong>{{ person.tropic }}<br>
                            <strong>Status: </strong>{{ person.status }}
                          </card-testimonial>
                        </div>
                      </card>
                    </links-page>
              </p>
            </div>

            <div class="tab-pane fade big-list" id="li4" role="tabpanel">
              <h4 class="pane-title" align="left">Research Activities</h4>
              <hr>
              <ul type="A">
                <li>Helium Exploration and Purification</li>
                <li>Geothermal Exploration</li>
                <li>Monitoring of Earthquake Precursors</li>
                <li>Nonlinear analysis of geochemical and geophysical data</li>
                <li>Theoretical Development</li>
              </ul>
              <p>Origin of 3He isotope in the inner Earth<br>Earthquake Precursor</p>
              <ul type="A">
                <strong><li>Helium Exploration and Purification :</li></strong>
                <p class="text-justify">Recently an unprecedented scarcity of helium is observed around the globe. The largest supplier of Helium, the United States of America already announced to cut off the supply to the other part of the globe. The helium used in scientific research and modern technology in India is 100% imported till the date. So far work has been done to extract helium from hot springs (surface manifestation only) only Bakreswar geothermal area. However the He yield from this existing plant is very less (Fig 1).
                <div class="geoimage">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra1.jpg" class="img img-responsive single-image">
                    <p class="text-center"><strong>Fig 1 : Helium Plant at Bakreswar</strong></p>
                </div>
                Therefore a deep drilling based helium extraction plant along with purification system is proposed to recover helium in large scale.In this scenario very recently NIT Durgapur has taken a programme to explore the hydrothermal source of helium at BakreswarTantloi geothermal area. A research project has been undertaken at Bakreswar-Tantloi geothermal area to extract helium in large scale from a proposed 800 m deep drilling (bore-hole).The raw helium (concentration of 1.8-2.0 vol.%, mixed with other gases like CH4 3.43 vol%, N2  92.20 vol%, Ar 2.10 vol%, O2 0.90 vol%, CO2 1.20 vol%,) which is supposed to be extracted from this 800 m deep bore-hole.
                <div class="geoimage">
                  <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra2.jpg" class="img img-responsive single-image">
                  <p class="text-center"><strong>Fig 2 : Deep drilling based Helium Plant at Bakreswar</strong></p>
                </div>
                After extraction of helium from that hot spring gas we need to purify it. In this purposes we must need to build a Helium Plant having a well-developed purification Units (Fig 2).<br>
                This purification unit will be designed  by the technique known as Pressure Swing Adsorption (PSA) to purify helium gas to obtain Grade A helium (Purity > 99.0 vol.%) that we can get high recovery rate  > 20-30%, otherwise it will not be usable at all in the modern equipments ,technology and science . Our aim is to fabricate this purification system by utilizing the adsorption properties of materials and PSA technique.
                </p>
                <strong><li>Geothermal Exploration :</li></strong>
                <p class="text-justify">
                  The project is a start off venture for exploring the Geothermal Energy and setting up a proposed Geothermal Power Plant in the Bakreswar-Tantloi Geothermal Area. The high geothermal heat outflow (230 mW/m2), geothermal gradient (90 0C/km) is seen in this area. Also high concentration of helium and radon (radioactive gas) are emanating from the hot springs of this zone. These data indicates the presence of a potential geothermal resource in the area. This area will be ideal for setting up a “geothermal” energy reactor - a vital source of energy (green energy) still completely ignored in India.
                  <div class="geoimage">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra3.jpg" class="img img-responsive single-image">
                  </div>
                  NIT Durgapur has taken up a project of drilling an 800m borehole which will supply the natural steam for the proposed Pilot Geothermal Plant. Different data analysis will be done at different depths in the borehole which will be useful for the installation of the equipments for the above mentioned Pilot Geothermal Power Plant. 
                   <div class="geoimage">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra4.jpg" class="img img-responsive multi-image">
                  
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra5.jpg" class="img img-responsive multi-image">
                  
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra6.jpg" class="img img-responsive multi-image">
                  </div>
                </p>
                <strong><li>Monitoring of Earthquake Precursors :</li></strong>
                <p class="text-justify">
                  The Earthquake Precursor Study will deploy gas geochemical techniques for the prediction of earthquake. It focusses in bringing together changes in spring gas and soil gas anomalies as a predictive tool in earthquake research by accessing instrumental data recorded at four geographically remote monitoring centres using digital data communication through VSAT networking.The principal objective of the research is to create baseline information on the relationship of gas concentration changes to imminent seismic events in the context of the Indian geophysical scenario. It proposes to examine inherent redundancies in the application of the method and the possibility of assimilating geochemically derived information with other predictive approaches.Statistical data correlation is a part of the investigation.Presently four Monitoring Stations are operated by the said group at different corners of the country along with a central data analysis centre at headquarter at NIT Durgapur. The monitoring stations are placed in dissimilar geological environments and in different seismic zones of the country. One of the monitoring stations is located at the thermal spring site at Bakreswar(23o 52’ 30” N; 87o22’ 30” E) which lies in the eastern part of the country in a moderate risk zone - seismic zone III. It is close to the extinct (115Ma) Rajmahalvolcanics of the Chotanagpur gneissic complex in West Bengal. The second one monitoring station is situated at the TattaPani(33o14’16”N, 74o24’43”E)thermal spring site which falls in the north-western part of the country in a high risk zone - seismic zone IV and it is located in a non-volcanic geothermal area that lies within the mountain folds of Jammu & Kashmir, situated in proximity to the Main Boundary Thrust (MBT) of the Lesser Himalayas.The third one is at the mud volcano, Baratang island (12007’ N;92047’E) of Andaman & Nicobar islands. Mud or Sedimentary volcanoes are cone shape mounds formed from fine mud eruption containing gases and acidic liquids with suspended fine sediments. Mud volcanoes do not involve magma eruption. Muddy materials from great depths are squeezed upward. The fourth is located at Tantlio Hot Spring site, Jharkhand. In each site, soil gases as well as hydrothermal gases are collected. Different kind of instruments such as gas chromatograph, radon monitor, seismometer etc. is installed at the said laboratories to collect the geochemical and geophysical data.   The recorded data are sent to the headquarter at NIT Durgapur through VSAT internet connectivity for further analysis.
                  <div class="geoimage">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra7.jpg" class="img img-responsive multi-image">
                  
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra8.jpg" class="img img-responsive multi-image">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra9.jpg" class="img img-responsive multi-image">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra10.jpg" class="img img-responsive multi-image">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra11.jpg" class="img img-responsive multi-image">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra12.jpg" class="img img-responsive multi-image">
                  </div>

                  <span><strong>1. NON LINEAR ANALYSIS OF GEOCHEMICAL AND GEOPHYSICAL DATA</strong></span><br>
                    Earthquake prediction is a challenging job for the global scientific community. Geochemical and geophysical precursor signals from the earth interior are basically non linear in nature .These signals contain information about the deep earth. Our knowledge about the various interacting features(physio-chemical processes) within the deep earth is very limited which causes a great deal of uncertainty in the field of earthquake prediction .By applying different kind of  non linear technique one may explore various information about  the physics of deep earth geochemical and geophysical processes. Earthquake prediction is a challenging job for the global scientific community. Geochemical and geophysical precursor signals from the earth interior are basically non linear in nature .These signals contain information about the deep earth. Our knowledge about the various interacting features(physio-chemical processes) within the deep earth is very limited which causes a great deal of uncertainty in the field of earthquake prediction .By applying different kind of  non linear technique one may explore various information about  the physics of deep earth geochemical and geophysical processes.<br>There are a number of non linear techniques by the help of which we can explore the various nature of the geochemical and geo physical data that we are getting from the various hot spring and volcanoes.<br>
                  The various non linear techniques that we are using are listed below:
                  <ul>
                    <li>Power spectrum analysis through FFT</li>
                    <li>Wavelet analysis through CWT / DWT (WAVELET TRANSFORM)</li>
                    <li>Nonlinear exponent – Embedding dimension, Correlation dimension etc. through 4.FRACTAL</li>
                    <li>Recurrence plot</li>
                    <li>Multifractal analysis</li>
                  </ul>
                  Nonlinear techniques were adopted on the recorded time series data to extract the information hidden in the helium and radon time series. Continuous wave let transform was applied on the radon time series recorded simultaneously at Bakreswar and TattaPani during the period of December 15-2007-January15, 2008. The localized contours present in the wave let of Bakreswar and TattaPani radon time series are the imprint of the pre-seismic anomalies. The wave let analysis shown in figure1 reveals the anomalies that were recorded in both the site during the period December24-27,2007.<br>
                  The variation of the time series data at hot spring is shown below<br>
                  <div class="geoimage">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra13.jpg" class="img img-responsive single-image">
                  </div><br>
                  In order to understand the underlying dynamics and nonl inearity involved in the physico-chemical processes of excess release of helium and radon prior to an earthquake the Fast Fourier Transform was applied to the recent soil radon time series data recorded at TattaPani hotspring site during July, 2009. Fig.2 shows the presence of long-range correlation in the radon time series data recorded at TattaPani during July, 2009. Multi-fractal statistics was also applied to the recent soil radon time series data recorded at TattaPani hotspring site during November 1-December30, 2012. Comparison of radon data for seismically active phase and seismically quiescent phase were made through the multi-fractal analysis. the fig.3 shows the multifractal spectrum of the time series data <br>
                  <div class="geoimage">
                  
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra14.jpg" class="img img-responsive multi-image">
                  
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra15.jpg" class="img img-responsive multi-image">
                    <img src="https://old.nitdgp.ac.in/helium_geothermal/images/ra16.jpg" class="img img-responsive multi-image">
                  </div>
                </p>
                <strong><li>Theoretical Development :</li></strong>
                <p>
                  <ul type="I">
                    <li><strong>Origin of 3He isotope in the inner Earth:</strong></li>
                    <p class="text-justify">
                      Continuous emanation of Helium isotopes (3He &4He) from geothermal springs has drawn our attention in the recent past. It is quite a puzzling situation to understand what the origin of these gasses is. The high 3He/4He (R) ratio indicates either there is a lack of the radiogenic helium isotope (4He) of excess of the primordial helium isotope (3He). The data of the 3He/4He ratio from various researchers around the globe indicate that the distribution of 3He/4He is not uniform throughout the various parts of earth. This unequal distribution brings us to question about the recently adopted model of earth’s accretion process.<br>
                      Another interesting situation is that 3He cannot be originated anywhere on earth through natural processes as per present day knowledge. We are thus forced to us ask how can there be such a huge reservoir of primordial helium that is continuously emanating at least for the past 2 billion years. All the 3He reservoirs around the globe are assumed to be originated during the accretion process of earth. But if that was the only source, the rate of emanation should have been decreasing over time which is not the case. So we our left with the option that probably there is source of 3He inside the earth itself. But as per recent geological construction of earth there’s no such scope for 3He generation. It is probable, that there is a natural geo-reactor running for the past 1.8 billion years. It is our endeavour to understand and establish a theoretical background for the origin of 3He in the earth’s interior.<br>
                      The background of this thought are based on the facts that firstly at Oklo, Gabon, Africa evidences of a naturally occurring fission geo-reactor was found which points out that in the planetary systems nuclear chain reactions can be initiated and sustained naturally without any exterior force. The second evidences of this prediction are the ever changing polarity of earth’s magnetic field. There can be a possible explanation of this planetary magnetic field’s origin by help of a nuclear geo-reactor at the centre of earth.<br>
                      Other basis is the fact that gas giants like Jupiter and Saturn are found to emanate twice as much energy than received by the sun. What is the origin of this excess energy?
                    </p>
                    <li><strong>Earthquake Precursor:</strong></li>
                    <p class="text-justify">Earthquakes are well known to be the after effect of plate tectonic movements, yet little is known about the true causes of tectonic movements. Also there is, at present, no perfect theory that unambiguously gives the exact origin and range of effect of such movements. </p>
                  </ul>
                </p>
              </ul>
            </div>

            <div class="tab-pane fade big-list" id="li5" role="tabpanel">
              <h4 class="pane-title" align="left">Equipment</h4>
              <hr>
              <div class="col-12 caro">
                <Carousel :slides="slides"></Carousel>
              </div>
            </div>

            <div class="tab-pane fade big-list" id="li6" role="tabpanel">
              <h4 class="pane-title" align="left">Field Visit Report</h4>
              <hr>              
              <p><strong>Report on :</strong></p>
                    Visit to<br>
                    Geochemical Monitoring Laboratory, at Bakreswar-Tantloi Geothermal Area, West Bengal & Jharkhand<br>
                    Date of Visit: August 23-24, 2015
                  <ul style="list-style-type:none;">
                    <li>
                      <a style="text-decoration: none;" target="new" href="https://old.nitdgp.ac.in/helium_geothermal/images/field_visit_report.pdf">
                        Download
                      </a>
                    </li>
                  </ul>
              
            </div>
            <div class="tab-pane fade big-list" id="li7" role="tabpanel">
              <h4 class="pane-title" align="left">Seminar</h4>
              <hr>              
              <table-renderer :theader="['Sl. No.','Duration','Name of the Institute/ Industry','Sponsored By','Name of the course','Name of the participant']" :table="seminers" />
            </div>
            <div class="tab-pane fade big-list" id="li8" role="tabpanel">
              <h4 class="pane-title" align="left">Publications</h4>
              <hr>
              <ul type="a">
                <li><strong>Paper publications in National / International Journals:</strong></li>
                <ul type="i">
                  <li><strong>In SCI Journals</strong></li>
                  <table-renderer :theader="['Sl. No.','Title of Paper','Author(s)','Name of the Journal','Vol. & Year','Pages']" :table="scijournels" />
                  <li><strong>Other than SCI Journals</strong></li>
                  <table-renderer :theader="['Sl. No.','Title of Paper','Author(s)','Name of the Journal','Vol. & Year','Pages']" :table="otherscijournels" />
                  <li><strong>Books/ Monographs/ Book chapters written: </strong></li>
                  <table-renderer :theader="['Sl. No.','Title','Book Name','Name of Coauthor,if any','Year of Publication','Publisher with address']" :table="monographs" />
                </ul>
                <p class="text-justify">
                  Full texts of all the publications are available on-line in Research Gate:   <a href="https://www.researchgate.net/profile/Hirok_Chaudhuri/publications/">https://www.researchgate.net/profile/Hirok_Chaudhuri/publications/</a> <br>
                  Google Scholar: <a href="http://scholar.google.co.in/citations?user=_X2gpvoAAAAJ&hl=en">http://scholar.google.co.in/citations?user=_X2gpvoAAAAJ&hl=en</a> 
                </p>                
                <li><strong>Papers publication in National/ international Conferences: </strong></li>                
                  <table-renderer :theader="['Sl. No.','Title of paper','Co-author(s), if any','Name of the Conference','Date & year']" :table="geoconferences" />
              </ul>
              <p class="text-justify">
                Abstract of all the conference publicationsare available on-line in Research Gate: <a href="https://www.researchgate.net/profile/Hirok_Chaudhuri/publications/">https://www.researchgate.net/profile/Hirok_Chaudhuri/publications/</a>  <br>
                Google Scholar: <a href="http://scholar.google.co.in/citations?user=_X2gpvoAAAAJ&hl=en">http://scholar.google.co.in/citations?user=_X2gpvoAAAAJ&hl=en</a> 
              </p>
            </div>
            <div class="tab-pane fade big-list" id="li9" role="tabpanel">
              <h4 class="pane-title" align="left">Photo Gallery</h4>
              <hr>
              <span style="color: red;">Photo gallery will be published soon.</span>
            </div>
            <div class="tab-pane fade big-list" id="li10" role="tabpanel">
              <h4 class="pane-title" align="left">Contact Us</h4>
              <p align="left">
                Dr. Hirok Chaudhuri<br>
                Project Manager, Helium and Geothermal Project & Associate Professor, <br>
                Department of Physics,<br>
                National Institute of Technology Durgapur,<br>
                Mahatma Gandhi Avenue,<br>
                Durgapur-713209, <br>
                West Bengal, India.<br>
              </p>
              <hr>
              <p align="left">
                <strong>Telephone : </strong>+91 343 2546808 (Office)<br>
                <strong>Cell Phone : </strong>+91 9434789019, +91 9830076271<br>
                <strong>Email : </strong>hirok.chaudhuri@phy.nitdgp.ac.in, chaudhuri_hirok@yahoo.co.in
              </p>
              <!--
              <hr>
              <div class="col testimonial">
                <div class="card testimonial-card text-center">
                  <div class="card-up">
                  </div>

                  <div align="center">
                    <img src="https://admin.nitdgp.ac.in/files/faculty/Hirok%20Chaudhuri/55.JPG" class="avatar mx-auto rounded-circle img-fluid">
                  </div>
                  <div class="card-body-in">
                    <p class="card-title">
                      <strong>
                        <a class="blue-text notranslate" href="https://old.nitdgp.ac.in/faculty/bed09767-49b2-4ed9-a5d8-aaefbeea9a40">
                          Dr. Hirok Chaudhuri
                        </a>
                      </strong>
                    </p>

                    <h6 class="black-text">Project Manager, Helium and Geothermal Project & Associate Professor, Department of Physics <br>National Institute of Technology Durgapur <br>Mahatma Gandhi Avenue, Durgapur-713209 <br>West Bengal, India</h6>
                    <hr>
                    <p class="min-profile">
                      <i class="fa fa-envelope"></i>&nbsp;&nbsp;&nbsp;hirok.chaudhuri@phy.nitdgp.ac.in , chaudhuri_hirok@yahoo.co.in<br>
                      <i class="fa fa-phone"></i>&nbsp;&nbsp;&nbsp+91 343 2546808 (Office) , +91 9434789019
                                   , +91 9830076271
                    </p>
                  </div>
                </div>
              </div> -->
            </div>
          </div>

        </div>
      </div>
    </sp-card>
    <div v-show="nav" id="fade" class="black_overlay"></div>
  </div>
</template>
<script>
import axios from 'axios'
import { genBackendURL, backURL } from '@/common.js'
import TableRenderer from '@/components/TableRenderer'
import CardCollapse from '@/components/CardCollapse'
import SpCard from '@/components/SpCard'
import Card from '@/components/Card'
import CardTestimonial from '@/components/CardTestimonial'
import LinksPage from '@/components/LinksPage'
import Carousel from '../Carousel'

export default {
  name: 'Geothermal',
  data () {
    return {
      general: true,
      windowWidth: 1000,
      extraNavClasses: [],
      nav: false,
      popUpTop: 0,
      top: -1,
      students:[
        {name:'Mr. CHIRANJIT MAJI',designation:'M. Sc. in Physics (2012-2014), Physics Department, Jadavpur University, Kolkata-32 ',image:'',email:'chiranjit.nitdphysics@yahoo.in',tropic:'Investigation on Geochemical and Geophysical Aspect of Geothermal Exploration at Bakreswar-Tantloi Geothermal Area',status:'Ongoing'},
        {name:'Ms. TAPAPRIYA GUPTA',designation:'M. Sc. in Applied Geology (2012-2014), Department of Geological Sciences, Jadavpur University, Kolkata-32 ',image:'',email:'tapapriyagupta@rediffmail.com',tropic:'nvestigation on Multi-parametric and Multi-station based Geochemical Precursors for Earthquakes',status:'Ongoing'},
        {name:'Ms. KANKANA SEAL',designation:'M. Tech. in Advanced Material Sci. & Tech. (2013-2015), Physics Department, NIT Durgapur.',image:'',email:'campus.kankana@gmail.com',tropic:'Purification of Hydrothermal Helium through Adsorption Technique',status:'Completed'},
        {name:'Mr. RITWIK DAS',designation:'Pursuing M. Tech. in Advanced Material Sci. & Tech.(2014-2016), Physics Department, NIT Durgapur.',image:'',email:'rik.das8@gmail.com',tropic:'Geothermal Exploration at Bakreswar Geothermal Area',status:'Ongoing'},
        {name:'Mr. RITESH KANT GUPTA',designation:'  Pursuing M. Tech. in Advanced Material Sci. & Tech.(2014-2016), Physics Department, NIT Durgapur',image:'',email:'ritesh110990@gmail.com',tropic:'Application of Geophysical and Geochemical Study in Helium Exploration at Bakreswar Geothermal Area',status:'Ongoing'},
        {name:'Ms. BIVA SHARMA',designation:'M. Sc. in Physics, (2013-2015) Physics Department, NIT Durgapur',image:'',email:' sharma.biva@gmail.com',tropic:'Application of Non-linear Techniques in Geochemical & Geophysical Precursors of Earthquake',status:'Completed'},
        {name:'Mr. SAMAPAN BHADURY',designation:'M. Sc. in Physics (2013-2015) Physics Department, NIT Durgapur',image:'',email:'sam18b@gmail.com',tropic:'Origin of He3 in the Earth Interior',status:'Completed'},
        {name:'Mr. SOUMYA MUKHERJEE',designation:'Perusing M. Sc. in Physics (2014-2016), Physics Department, NIT Durgapur.',image:'',email:'reach2soumya28@gmail.com',tropic:'Investigation on Nonlinearity in EarthquakePrecursory Signals',status:'Ongoing'},
        {name:'Mr. SOUMYA MUKHERJEE',designation:' Perusing M. Sc. in Physics (2014-2016), Physics Department, NIT Durgapur.',image:'',email:'reach2soumya28@gmail.com',tropic:'Mud Volcano Gamma Burst: A PossiblePrecursor to Earthquake',status:'Completed'},
        {name:'Mr. SOMEN ADHIKARY',designation:'Perusing M. Sc. in Physics (2014-2016), Physics Department, NIT Durgapur.',image:'',email:'adhikary.somen@gmail.com',tropic:'Imprints of Gamma Dose Rate at Geothermal and Non-geothermal Provinces',status:'Completed'}
      ],
      faculties:[
        {name:'Dr. H. Chaudhuri',designation:'Project Manager, Helium and Geothermal Project & Assistant Professor, Physics Department, NIT Durgapur',specility:'Physicist'},
        {name:'Prof. T. Kumar ',designation:'Director, NIT Durgapur',specility:'Petroleum Engineer'},
        {name:'Prof. N. K. Roy',designation:'Professor, Electrical Engineering Department, NIT Durgapur',specility:'Electrical Engineer'},
        {name:'Prof. A. Gangopadhyaya',designation:'Professor, Earth & Environmental StudiesDepartment, NIT Durgapur',specility:'Geologist'},
        {name:'Dr. Kalyan Adhikari',designation:'Associate Professor, Earth & Environmental Studies Department, NIT Durgapur',specility:'Geologist'},
      ],
      advisors:[
      {name:'Prof. Bikash Sinha',designation:'Emeritus Professor at NIT Durgapur and INSA Eminent Scientist and Former Chairperson BOG, NIT Durgapur and Former Director, SINP, Kolkata & VECC, Kolkata',specility:'Physicist'},
      {name:'Prof. Amalendu Bhushan Bhattacharyya',designation:'Chairperson BOG, NIT Durgapur and Former Faculty Department of Physics, IIT Delhi, Delhi and Former Director, Institute of Technology and Management, Gurgaon andFormer Director, VLSI Design Programme, GOA University.',specility:'Physicist'}
      ],
      members:[
        {name:'Mr. Prithwijit Roy',designation:'Technician',location:'Tantloi Site ( Jharkhand )'},
        {name:'Mr. Sumit Khajuria',designation:'Technician',location:'TattaPani ( Jammu & Kasmir )'},
        {name:'Mr. Dhavinder Kumar',designation:'Attendant',location:'TattaPani ( Jammu & Kasmir )'},
        {name:'Mr. Suresh Kumar',designation:'Watch Man',location:'TattaPani ( Jammu & Kasmir )'},
        {name:'Mr. Galib Hussain',designation:'Watch Man',location:'TattaPani ( Jammu & Kasmir )'},
        {name:'Mr. Filix Ekka',designation:'Technician',location:'Baratang ( Andaman & Nicobar )'},
        {name:'Mr. Kamil Baa',designation:'Attendant',location:'Baratang ( Andaman & Nicobar )'},
        {name:'Mr. Sudhir Kandulana',designation:'Watch Man',location:'Baratang ( Andaman & Nicobar )'},
        {name:'Mr. Prakul Minj',designation:'Watch Man',location:'Baratang ( Andaman & Nicobar )'}
      ],
      slides:[
        {primary_caption:'Soil gas monitoring set up (schematic diagram) to monitor gas concentration is sub-soil gas',secondary_caption:'Soil gas monitoring set up (schematic diagram) to monitor gas concentration is sub-soil gas',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image019.jpg'},
        {primary_caption:'Hot spring gas monitoring set up to monitor gas concentration is hot spring',secondary_caption:'Hot spring gas monitoring set up to monitor gas concentration is hot spring',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image020.jpg'},
        {primary_caption:'RAIN GAUGE to monitor rain fall',secondary_caption:'RAIN GAUGE to monitor rain fall',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image021.gif'},
        {primary_caption:'RADON MONITOR (ALPHA GUARD) to monitor radioactive gas Radon-222 in hot spring',secondary_caption:'RADON MONITOR (ALPHA GUARD) to monitor radioactive gas Radon-222 in hot spring',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image022.jpg'},
        {primary_caption:'Soil Gas Radon Detector (BARASOL)to monitor radioactive gas Radon-222 in sub soil',secondary_caption:'Soil Gas Radon Detector (BARASOL)to monitor radioactive gas Radon-222 in sub soil',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image023.jpg'},
        {primary_caption:'GAMMA RAY MONITOR (GAMMA TRACER) monitor ambient gamma',secondary_caption:'GAMMA RAY MONITOR (GAMMA TRACER) monitor ambient gamma',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image024.gif'},
        {primary_caption:'Radon Progeny meter',secondary_caption:'Radon Progeny meter',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image025.gif'},
        {primary_caption:'Broad Band SEISMOMETER (in collaboration with IISER, Kolkata)',secondary_caption:'Broad Band SEISMOMETER (in collaboration with IISER, Kolkata)',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image026.jpg'},
        {primary_caption:'Gas Chromatograph to monitor Helium, Argon, Methane in hot spring gas and sub-soil gas',secondary_caption:'Gas Chromatograph to monitor Helium, Argon, Methane in hot spring gas and sub-soil gas',image:'https://old.nitdgp.ac.in/helium_geothermal/images/clip_image027.jpg'}
      ],
      seminers:[
        {sl:'1',duration:'Nov 10th to Dec 16th, 2015',institute:'Sri Mata Vaishno Devi University, Katra, J&K & IISER Kolkata',sponsor:'SERC',course:'Earthquake Hazard: Basic Approaches, Field Investigations and Modeling',participent:'Mr. Ritwik Das(M. Tech. Student)'},
        {sl:'2',duration:'Oct 27th to 31st, 2015',institute:'Kumaraguru College of Technology, Coimbatore,Tamil Nadu',sponsor:'IISc. Bangalore',course:'Conference: National Symposium on Instrumentation',participent:'Mr. Ritwik Das(M. Tech. Student),Mr. Ritesh Kant Gupta,(M. Tech. Student), Mr. Avishek Kumar(M. Tech. Student)'},
        {sl:'3',duration:'Aug 31st to Sep 04th ,2015',institute:'Dresden University of Technology, Dresden, Germany',sponsor:'Dresden University of Technology & SARAD GmbH, Germany ',course:'International Conference: 7th Dresden Symposium Hazard - Detection and Management',participent:'Dr.Hirok Chaudhuri'},
        {sl:'4',duration:'May 25th to 30th ,2015',institute:'IISER-Pune, Pune, Maharashtra ',sponsor:'Indo–US Science & Technology Programme',course:'Workshop: Time Series Analysis',participent:'Miss. Biva Sharma(M.Sc. Student)'},
        {sl:'5',duration:'Mar 23rd to 27th ,2015',institute:'Department of Applied Physics, Indian School of Mines, Dhanbad, Jharkhand',sponsor:'MNRE, Govt. of India',course:'Short Term Course : National Training Programme on Advances in New and Renewable Energy Materials and Technology',participent:'Dr.Hirok Chaudhuri; Miss. Tapapriya Gupta(PhD Student), Miss. Kankana Seal(M. Tech. Student)'},
        {sl:'6',duration:'Dec 28th to 30th , 2014',institute:'NIT Durgapur, WB',sponsor:'-',course:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disaster',participent:'Hirok Chaudhuri, Miss. Kankana Seal(M. Tech. Student),Miss. Biva Sharma(M.Sc. Student), Mr. SamapanBhadury(M.Sc. Student),Ritwik Das(M. Tech. Student),Mr. Ritesh Kant Gupta(M. Tech. Student)'}
      ],
      scijournels:[
        {sl:'1',paper:'Helium Potential in geothermal resources in India ',author:'Hirok Chaudhuri and D. Chandrasekharam ',journal:'Geothermal Energy Science',year:'2015',page:'Under Review'},
        {sl:'2',paper:'The Essence of Multifractal Detrended Fluctuation Technique to Analyse the Dynamics of Pre-seismic Soil Radon Time Series',author:'Chiranjib Barman, Hirok Chaudhuri, Argha Deb, Debasis Ghose, Bikash Sinha',journal:'Natural Hazards',year:'Vol. 78 (2) 2015',page:'855-877'},
        {sl:'3',paper:'Multifractal Detrended Fluctuation Analysis of Seismic Induced Radon-222 Time Series ',author:'Chiranjib Barman, Hirok Chaudhuri, Debasis Ghose, Argha Deb, Bikash Sinha ',journal:'Journal of Earthquake Science',year:'Vol. 1, 2014',page:'1-21'},
        {sl:'4',paper:'Long range correlation in earthquake precursory signals ',author:'H. Chaudhuri, C. Barman, A. N. S. Iyengar, D. Ghose, P. Sen, B. Sinha',journal:'The European Physical Journal, Special Topics',year:'Vol. 222, Issue 3-4, 2013',page:'827-838'},
        {sl:'5',paper:'Network of seismo-geochemical monitoring observatories for earthquake prediction research in India',author:'Hirok Chaudhuri, Chiranjib Barman, A. N. Sekar Iyengar, Debasis Ghose, Prasanta Sen and Bikash Sinha',journal:'ActaGeophysica',year:'Vol. 61, Issue 4, 2013',page:'1000-1025'},
        {sl:'6',paper:'A geochemical approach to earthquake reconnaissance at the Baratang mud volcano, Andaman and Nicobar Islands',author:'Hirok Chaudhuri, Debasis Ghose, Rakesh K. Bhandari, Prasanta Sen and Bikash Sinha',journal:'Journal of Asian Earth Sciences',year:'Vol. 46, 2012',page:'52–60'},
        {sl:'7',paper:'Long range gas-geochemical anomalies of a remote earthquake recorded simultaneously at distant monitoring stations in India on the multi-parametric and multi-station geochemical signatures for the earthquake prediction ',author:'Hirok Chaudhuri,Wassem Bari, Nasser Iqbal, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha ',journal:'Geochemical Journal',year:'Vol. 45, 2011',page:'1-156'},
        {sl:'8',paper:'The Enigma of Helium',author:'H Chaudhuri, D Ghose, R. K. Bhandari, P. Sen and B. Sinha',journal:'ActaGeodaetica et GeophysicaHungerica ',year:'Vol. 45(4), 2010',page:'452–470'},
        {sl:'9',paper:'Radon activity measurements around Bakreswar Thermal Springs ',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',journal:'Radiation Measurements',year:'Vol. 45, 2010',page:'143-146'},
        {sl:'10',paper:'Purification of Helium from Natural Gas by Pressure Swing Adsorption ',author:'Nisith K. Das, Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',journal:'Current Science',year:'Vol. 95, No. 12, 2008',page:'1684-1687'},
        {sl:'11',paper:'Implications of geochemical precursory Signals vis a vis Earthquakes',author:'N. K. Das, H Chaudhuri,R. K. Bhandari, D. Ghose, P Sen and B. Sinha',journal:'Geophysical Research Abstracts',year:'Vol. 9, 2007',page:'00102'},
        {sl:'12',paper:'Scaling and Crossover phenomena in pre-seismic helium signal ',author:'N. K. Das, H Chaudhuri,R. K. Bhandari, D. Ghose, P Sen and B. Sinha',journal:'Geophysical Research Abstracts',year:'Vol. 9, 2007',page:'00103'},
        {sl:'13',paper:'Nonlinear analysis of radon time series related to earthquake',author:'N. K. Das, H Chaudhuri, R. K. Bhandari, D. Ghose, P Sen and B. Sinha',journal:'Modeling Critical and Catastrophic Phenomena in Geosciences, Lecture Notes in Physics',year:'Vol. 705, 2007',page:'481-490'},
        {sl:'14',paper:'Continuous monitoring of 222Rn and Its progeny at a remote station for seismic hazard surveillance',author:'Nisith K. Das, Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',journal:'Radiation Measurements',year:'Vol. 41, 2006',page:'634-6'},
      ],
      otherscijournels:[
        {sl:'1',paper:'Multi-parametric and Multi-station Facility for Earthquake Precursory Study',author:'Hirok Chaudhuri and D. Chandrasekharam ',journal:'Bhoo-Kampan, Newsletter of Indian Society of Earthquake Science',year:'Vol. 2, Issue 2, 2013 ',page:'1─2'}
      ],
      monographs:[
        {sl:'1',title:'Radon and helium fluctuations prior to seismic events in thermal spring gas',book:'Electromagnetic Phenomenon Related to Earthquakes & Volcanoes',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',year:'pp 147-155, 2007 ',address:'Narosa Publishing House, ISBN: 978-81-7319-858-8'},
        {sl:'2',title:'Observation of pre-seismic signals through geochemical monitoring',book:'Recent Development in Disaster Management',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',year:'pp 67-75, 2007',address:'Pragati Publication, ISBN: 81-8064-1-6'},
        {sl:'3',title:'Geo-chemical and Geophysical Techniques for Seismic Surveillance',book:'Recent Development in Disaster Management',author:'Nisith K. Das, Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha ',year:'pp 60-, 2007',address:'Pragati Publication,ISBN: 81-8064-1-6'},
      ],
      geoconferences:[
        {sl:'1',paper:'Earthquake Precursory Signals at TattaPani Hot Spring Site, J&K',author:'Hirok Chaudhuri',conference:'Earthquake Hazard: Basic Approaches, Field Investigations and Modeling ',year:'November 10-16, 2015'},
        {sl:'2',paper:'Simple Instrumentation for the Study of Complex Earthquake',author:'Ritesh Kant Gupta,Hirok Chaudhuri',conference:'Conference of National Symposium on Instrumentation (NSI 40), held at Kumaraguru College of Technology, Coimbatore',year:'October 30-31, 2015'},
        {sl:'3',paper:'Data Automation for Online Earthquake Precursory Signals',author:'Avishek Kumar, Hirok Chaudhuri',conference:'Conference of National Symposium on Instrumentation (NSI 40), held at Kumaraguru College of Technology, Coimbatore',year:'October 30-31, 2015'},
        {sl:'4',paper:'Non-Linear Analysis of Geochemical Precursor for Earthquake',author:'Ritwik Das, Ritesh Kant Gupta, Hirok Chaudhuri',conference:'Conference of National Symposium on Instrumentation (NSI 40), held at Kumaraguru College of Technology, Coimbatore',year:'October 30-31, 2015'},
        {sl:'5',paper:'Nonlinearity in Earthquake Precursory Signals',author:'Hirok Chaudhuri',conference:'International Conference: 7th Dresden Symposium-Hazard Detection and Management held at Dresden University of Technology and SARAD GmbH, Germany',year:'August 31, 2015-September 04, 2015'},
        {sl:'6',paper:'Noble Gas Helium – A Tool for Earthquake Precursors',author:'Kankana Seal, Hirok Chaudhuri',conference:'International Conference: 7th Dresden Symposium-Hazard Detection and Management held at Dresden University of Technology and SARAD GmbH, Germany',year:'August 31, 2015-September 04, 2015'},
        {sl:'7',paper:'Non-Linear Analysis of Earthquake Precursors',author:'Biva Sharma, Hirok Chaudhuri',conference:'Time Series Analysis Workshop, Indo-US Science & Technology Programme held at IISER Pune',year:'May 25-30, 2015'},
        {sl:'8',paper:'Helium from geothermal sources',author:'Hirok Chaudhuri, Bikash Sinha, D. Chandrasekharam',conference:'World Geothermal Congress 2015 To be held at Melbourne, Australia (International Conference)',year:'April  19-25, 2015'},
        {sl:'9',paper:'Multi-station and multi-parametric approach for the study of geochemical precursors for earthquakes – Indian scenario',author:'Hirok Chaudhuri',conference:'International Conference, International Geo-hazard Research Symposium, IGRS 2014 held at NASA Ames Research Center, California (International Conference)',year:'December 10-12, 2014'},
        {sl:'10',paper:'Geochemical  Precursor for Earthquake ',author:'Hirok Chaudhuri',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB (International Conference)',year:'December 28-30, 2014'},
        {sl:'11',paper:'Nonlinear technique adopted in earthquake precursor study ',author:'Biva Sharma, Ritesh Kant Gupta, Kankana Seal, Samapan Bhadury, Ritwik Das , Hirok Chaudhuri ',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB (International Conference)',year:'December 28-30, 2014'},
        {sl:'12',paper:'Helium Crisis ',author:'Samapan Bhadury, Ritwik Das, Kankana Seal, Biva Sharma, Ritesh Kant Gupta, Hirok Chaudhuri ',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB (International Conference)',year:'December 28-30, 2014'},
        {sl:'13',paper:'Geochemical  Precursor for Earthquake',author:'Kankana Seal, Ritesh Kant Gupta, Ritwik Das, BivaSharma,Samapan Bhadury, Hirok Chaudhuri',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB',year:'December 28-30, 2014'},
        {sl:'14',paper:'Analysis of earthquake precursors through FFT techniques',author:'Ritesh Kant Gupta, Ritwik Das, Kankana Seal, Biva Sharma, Samapan Bhadury, Hirok Chaudhuri ',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB (International Conference)',year:'December 28-30, 2014'},
        {sl:'15',paper:'Analysis of earthquake through wavelet techniques',author:'Ritwik Das, Ritesh Kant Gupta, Samapan Bhadury, Kankana Seal, Biva Sharma, Hirok Chaudhuri ',conference:'International Conference on Decision Support Systems for Early Warning and Mitigation of Disasterheld at NIT Durgapur, WB (International Conference)',year:'December 28-30, 2014'},
        {sl:'16',paper:'Essence of EMD & HHT in analyzing Seismo- geochemical precursory signal',author:'Chiranjib Barman, Hirok Chaudhuri, Debasis Ghose, Bikash Sinha',conference:'Advances in Earthquake Science (AES III, 2014) held at  ISR , Gandhinagar, Gujarat (International Conference)',year:'January 4-6, 2014'},
        {sl:'17',paper:'Exploration of Earthquake Precursory Signals by Non-linear Techniques',author:'Hirok Chaudhuri',conference:'8th Conference on Nonlinear Systems and Dynamics held at Indore IIT, Indore (International Conference)',year:'December 11- 14, 2013'},
        {sl:'18',paper:'Analysis of radon-222 time series data using Empirical Mode Decomposition based Hilbert Huang Transform',author:'Chiranjib Barman, Hirok Chaudhuri, Debasis Ghose, Bikash Sinha',conference:'8th Conference on Nonlinear Systems and Dynamics held at Indore IIT, Indore (International Conference) ',year:'December 11- 14, 2013'},
        {sl:'19',paper:'Nonlinear time series analysis of geochemical emissions using recurrence plots',author:'VramariMitra, A.N. SekarIyengar, Hirok Chaudhuri',conference:'8th Conference on Nonlinear Systems and Dynamics held at Indore IIT, Indore (International Conference)',year:'December 11- 14, 2013'},
        {sl:'20',paper:'Geothermal Potential of Bakreswar-Tantloi hydrothermal system',author:'Hirok Chaudhuri and Bikash Sinha ',conference:'International Conference: “Geothermal Energy Initiative & Development - One day seminar on issues & challenges in geothermal energy” held at PanditDeendayal Petroleum University, Gujarat (International Conference)',year:'July 26, 2013'},
        {sl:'21',paper:'Study of Geochemical Precursors for Earthquakes in Indian Geothermal fields',author:'Hirok Chaudhuri, Chiranjib Barman, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'7th Dresden Symposium "Hazards - Detection and Management" held at Dresden, Germany (International Conference)',year:'March 3-8, 2013'},
        {sl:'22',paper:'Multifractal Detrended Fluctuation Analysis of seismic induced radon-222 time series',author:'Chiranjib Barman, Hirok Chaudhuri, Debasis Ghose, Prasanta Sen, Bikash Sinha',conference:'Advances in Earthquake Science (AES II, 2013) held at  ISR , Gandhinagar, Gujarat (International Conference)',year:'February 1-2, 2013'},
        {sl:'23',paper:'An Overview of Helium and Radon Release at Bakreswar and TattaPani Geothermal Areas',author:'Hirok Chaudhuri, Chiranjib Barman, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'Advances in Earthquake Science (AES II, 2013) held at  ISR , Gandhinagar, Gujarat (International Conference)',year:'February 1-2, 2013'},
        {sl:'24',paper:'Radon and Helium Studies as Earthquake Precursors in the Context of Indian Scenario',author:'Hirok Chaudhuri, Chiranjib Barman, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'National Conference on Natural Hazards and Mitigation held at Eshan College, Mathura, UP (National Conference)',year:'December 4 - 5, 2012 '},
        {sl:'25',paper:'Data automation software to monitor continuous and on-line signals for earthquake precursors',author:'Chiranjib Barman, Hirok Chaudhuri, Debasis Ghose, Prasanta Sen and Bikash Sinha ',conference:'National Conference on Natural Hazards and Mitigation held at Eshan College, Mathura, UP (National Conference)',year:'December 4 - 5, 2012'},
        {sl:'26',paper:'Seismo-geochemical algorithm for earthquake precursor ',author:'Hirok Chaudhuri, Chiranjib Barman, A. N. SekarIyengar, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'49th annual convention of Indian Geophysical Union (IGU) held at PDPU Gandhinagar (National Conference)',year:'October 29-31, 2012'},
        {sl:'27',paper:'Long range correlation in earthquake precursory signals',author:'H. Chaudhuri,C. Barman, A. N. S. Iyengar, D. Ghose, P. Sen, B. Sinha',conference:'National Conference on Nonlinear Systems and Dynamics held at IISER Pune (National Conference) ',year:'July 12-15, 2012.'},
        {sl:'28',paper:'Detection of earthquake precursors by wavelet analysis of seismo-geochemical signals ',author:'Chiranjib Barman, Hirok Chaudhuri, A. N. SekarIyengar',conference:'National Conference on Nonlinear Systems and Dynamics held at IISER Pune (National Conference) ',year:'July 12-15, 2012'},
        {sl:'29',paper:'Network of seismo-geochemical monitoring observatories for earthquake prediction research in India',author:'Hirok Chaudhuri, Chiranjib Barman, A. N. SekarIyengar, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'Third International Geo-Hazards Research Symposium (IGRS-2012), held at HNB Garhwal University, Teheri, Garhwal, Uttarakhand, (International Conference)',year:'June 10-14, 2012'},
        {sl:'30',paper:'Power Spectrum analysis of multi-parameter gas-geochemical precursory signals of the Pakistan earthquake recorded at thermal spring emanation at TattaPani, Jammu & Kashmir, India',author:'Hirok Chaudhuri, Chiranjib Barman, A. N. SekarIyengar, Debasis Ghose, Rakesh K. Bhandari, Prasanta Sen and Bikash Sinha',conference:'International Conference on Complex Dynamical System and Applications (CDSA – II) held at Presidency College, Kolkata (International Conference)',year:'January 9-11, 2012'},
        {sl:'31',paper:'Study of multi-parameter gas-geochemical precursor signals of a distant earthquake recorded simultaneously at two thermal springs in India',author:'H. Chaudhuri, D. Ghose, R. K. Bhandari, P. Sen, and B. Sinha,',conference:'International Symposium on The 2001 Bhuj Earthquake and Advances in Earthquake Science (AES I, 2011) held at Institute of Seismological Research (ISR), Gandhinagar, Gujarat (International Conference)',year:'January 22 – 27, 2011'},
        {sl:'32',paper:'Pre-seismic geo-chemical signatures to distant earthquakes ',author:'Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'International Workshop on Earthquake Precursors held at National Geophysical Research Institute (NGRI), Hyderabad (International Conference)',year:'November 25-27, 2010'},
        {sl:'33',paper:'Time series analysis of the Helium-Radon precursors observed simultaneously at two thermal spring sites in India before the distant 6.3M China earthquake',author:'Hirok Chaudhuri, A. N. SekharIyengar,Waseem Bari, Naseer Iqbal, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen, and Bikash Sinha',conference:'International Workshop on Seimo-electromagnetics and Atmospheric Science (IWSE-AS)held at RBS Engineering College, Agra (International Conference)',year:'November 16-18,2010'},
        {sl:'34',paper:'Earthquake Precursor Study Through Time Series Analysis of Thermal Spring Emanated Radon and Gamma Signal',author:'H Chaudhuri, S. Mir, W. Bari, N. Iqbal, N. K. Das, D. Ghose, P. Sen',conference:'National level Conference on Earthquake Prediction: Recent Developments & Challenges held at Kashmir University, Srinagar (National Conference)',year:'August 06-07, 2008'},
        {sl:'35',paper:'Earthquake Precursors – Indian Initiatives',author:'Nisith K. Das, Amitava Sur, Hirok Chaudhuri, Rakesh K. Bhandari, Prasanta Sen, Debasis Ghose and Bikash Sinha',conference:'National level Conference on Earthquake Prediction: Recent Developments & Challenges held at Kashmir University, Srinagar (National Conference)',year:'August 06-07, 2008'},
        {sl:'36',paper:'Earthquake precursor study through time series analysis of thermal spring emanated radon and gamma signal at TattaPani Site, Rajouri',author:'S. Mir, H. Chaudhuri, W. Bari, N. Iqbal',conference:'National level Conference on Earthquake Prediction: Recent Developments & Challenges held at Kashmir University, Srinagar (National Conference)',year:'August 06-07, 2008'},
        {sl:'37',paper:'Observation of pre-seismic signals through monitoring of radon profile',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'National Symposium on Radiation Physics – 17Saha Institute of Nuclear Physics, Kolkata (National Conference)',year:'November 14-16, 2007'},
        {sl:'38',paper:'Observation of pre-seismic signals through geochemical monitoring ',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'National Seminar on “Recent Development in Disaster Management: Indian Perspective” held at Suri Vidyasagar College, Suri, Birbhum, W.B. (National Conference)',year:'November 24-25, 2006'},
        {sl:'39',paper:'Geo-chemical and Geophysical Techniques for Seismic Surveillance',author:'Nisith K. Das, Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'National Seminar on “Recent Development in Disaster Management: Indian Perspective” held at Suri Vidyasagar College, Suri, Birbhum, W.B. (National Conference)',year:'November 24-25, 2006'},
        {sl:'40',paper:'Radon and helium fluctuations prior to seismic events in thermal spring gas',author:'Hirok Chaudhuri, Nisith K. Das, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'International Workshop on Electromagnetic Studies Related to Earthquakes & Volcanoes held at RBS Engineering College, Agra (International Conference)',year:'November 20-22, 2006'},
        {sl:'41',paper:'Probing Radon and Gamma for Detection of Precursory Signature to Earthquake',author:'Nisith K. Das, Hirok Chaudhuri, Rakesh K. Bhandari, Debasis Ghose, Prasanta Sen and Bikash Sinha',conference:'National Symposium on Radiation Physics – 16 held at Menakshi Women College, Chennai (National Conference)',year:'January 18-20, 2006'},
        {sl:'42',paper:'Nonlinear analysis of radon time series related to earthquake',author:'N. K. Das, H Chaudhuri, R. K. Bhandari, D. Ghose, P Sen and B. Sinha',conference:'International Workshop on Models of Earthquake: Physics Approaches held at Saha Institute of Nuclear Physics, Kolkata (International Conference)',year:'December 13-16, 2005'}
      ]
    }
  },
  created () {
    this.$emit('hideloader', true)
    window.addEventListener('resize', this.updateWidth)
    this.windowWidth = document.body.clientWidth
  },
  mounted () {
    Array.from(document.getElementsByClassName('dropdown-item')).forEach(el => {
      el.addEventListener('click', this.hideNav)
    })
  },
  methods: {
    hideNav () {
      this.nav = false
      this.extraNavClasses = []
      this.popUpTop = 0
    },
    showNav (event) {
      this.extraNavClasses = ['lift', 'div-block']
      this.nav = true
      this.popUpTop = event.clientY + this.top
      console.log(this.popUpTop)
    },
    getClassContent () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-8'
      else if (width > 900)
        return 'col-7'
      else if (width > 600) {
        this.top = -1
        return 'col-8'
      }
      else {
        this.top = 1
        return 'col-12'
      }
    },
    getClassNav () {
      let width = this.windowWidth
      if (width > 1180)
        return 'col-2'
      else if (width > 900)
        return 'col-3'
      else
        return 'div-none'
    },
    updateWidth () {
      this.windowWidth = document.body.clientWidth
    }
  },
  components: {
    TableRenderer,
    CardCollapse,
    SpCard,
    Card,
    Carousel,
    CardTestimonial,
    LinksPage
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateWidth);
  }
}
</script>

<style scoped>
  .staffs {
    min-width: 200px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
  .list-group a, .list-group a:hover {
    white-space: pre-wrap;
  }
  .dropdown-item:hover{
    background-color: #001333!important;
    color: #fff!important;
  }
  .photo {
    text-align: center;
  }
  .downc {
    margin: 0 auto;
    padding: 10px;
  }
  .btn {
    background: #001333;
    width: 50px;
    padding: 10px;
    float: right;
    margin-left: auto;
    margin-bottom: 0px;
  }
  .single-image{
    width: 100%;
  }
  .multi-image{
    width: 32%;
  }
  .geoimage{
      width: 100%;
  }
  .card-pic .caro-wrap {
    height: 380px;
    background: -webkit-gradient(linear,left top, left bottom,from(#03A9F4),color-stop(#039BE5),color-stop(#039BE5),to(#039BE5));
    background: linear-gradient(#03A9F4,#039BE5,#039BE5,#039BE5);
  }
  element {

}
.carousel-item {

    height: 100%;

}
.anim1 {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-name: fadeIn;
    animation-name: fadeIn;
    -webkit-animation-delay: 0s;
    animation-delay: 0s;
    -webkit-animation-timing-function: initial;
    animation-timing-function: initial;
    -webkit-animation-iteration-count: initial;
    animation-iteration-count: initial;
    -webkit-animation-direction: initial;
    animation-direction: initial;
    -webkit-animation-fill-mode: initial;
    animation-fill-mode: initial;
    -webkit-animation-play-state: initial;
    animation-play-state: initial;
}
.carousel-item {
    display: none;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    width: 100%;
    transition: -webkit-transform .6s ease;
    -webkit-transition: -webkit-transform .6s ease;
    transition: transform .6s ease;
    transition: transform .6s ease, -webkit-transform .6s ease;
    transition: transform .6s ease,-webkit-transform .6s ease;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    perspective: 1000px;
}
.carousel, .carousel-inner, .carousel-item {
    position: relative;
}

  @media screen and (min-width: 909px) {
    .btn {
      display: none;
      height: 0px;
    }
    .geoimage{
      width: 100%;
    }
  }
  @media screen and (max-width: 512px) {
    .geoimage{
      width: 100%;
    }
  }
  
  .lift {
    position: absolute;
    left: 10%;
    width: 80%;
    background-color: white;
    z-index: 2;
    overflow: auto;
  }
  .black_overlay {
    position: absolute;
    top: 0%;
    left: 0%;
    bottom: 0%;
    width: 100%;
    height: 100%;
    z-index: 1;
    background-color: black;
    -moz-opacity: 0.8;
    opacity: .80;
    filter: alpha(opacity=80);
  }
  .dropdown-item.faculty-login {
    background-color: #8f8;
  }
  .dropdown-item.faculty-login:hover {
    background-color: #0f0!important;
  }
  .col.testimonial {
    min-width: 200px;
    min-height: 100px;
    max-width: 320px;
    max-height: 500px;
    padding: 7px;
  }
  .min-profile {
    font-size: 72% !important;
  }
  hr {
    margin-left: 2em !important;
    margin-right: 2em !important;
  }
  .card-body-in .card-title .notranslate {
    font-size: 88% !important;
  }
  .card-body-in h6{
    font-size: 80% !important;
  }
  .testimonial-card .desig{
    font-size: 100%;
  }
  .testimonial-card .card-title{
    font-size: 100%;
  }
  .testimonial-card {
    min-height: 100% !important;
    min-width: 100% !important;
  }
  .card-up {
    height: 80px !important;
  }
  .card-up {
    background: linear-gradient(to right,#001333,#324e7d) !important;
  }
  .avatar {
    height: 100px !important;
    width: 100px !important;
  }
</style>
