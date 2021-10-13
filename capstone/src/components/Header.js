import React from 'react';

export const Header = (props) => {
  
  const logingHandler = () => {
    fetch("login")
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result, 'res')
        },
        // Примечание: важно обрабатывать ошибки именно здесь, а не в блоке catch(),
        // чтобы не перехватывать исключения из ошибок в самих компонентах.
        (error) => {
          console.log(error, 'err')
        }
      )
  }

    return (
       <header className="header">
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <a className="navbar-brand" href="#">Capstone</a>
          <div>

          <ul className="navbar-nav mr-auto">
            { props.isLoggedIn ? 
              <div>
                <li className="nav-item">
                  <a className="nav-link" href="#">{ props.username }</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">All Posts</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="">Log Out</a>
                </li> 
              </div>
              :
              <div>
                <li className="nav-item">
                    <a className="nav-link" id='login' href="#">Log In</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Register</a>
                </li> 
              </div>
          }
               
              </ul>
            </div>
          </nav>
      </header>
   )
};
