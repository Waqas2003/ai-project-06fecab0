import React from 'react';
import './App.css';
import Header from './components/Header';
import Projects from './components/Projects';
import About from './components/About';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <Projects />
      <About />
      <Footer />
    </div>
  );
}

export default App;