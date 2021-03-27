import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.css';
import {BrowserRouter, Route} from "react-router-dom";
import Switch from "react-bootstrap/Switch";
import Login from "./containers/Login";
import Forgot from "./containers/Forgot";

ReactDOM.render(
  <React.StrictMode>
      <BrowserRouter forceRefresh={true}>
          <Switch>
              <Route path="/login">
                  <Login/>
              </Route>

              <Route path="/forgot">
                  <Forgot/>
              </Route>
          </Switch>
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);