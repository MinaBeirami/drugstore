import React, { Component } from 'react';
import './App.css';
import { connect } from 'react-redux';
import Map from './Map';

class App extends Component {

  render() {
    return (
      <div className="MyMap" >

        <Map />
        
      </div>
    );
  }
}



export default App;
