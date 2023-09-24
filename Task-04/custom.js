class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <header>
      <div class="logo"><a href="Imaginedragons.html"><img class="blah" src="img/logo.png" alt="" width="35px" height="35px"></a>
         
      </div> 
      <nav>
          <ul class="links">
              <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q?si=Gel1D0CkRaShWhlup3Y8ww">
                  <i class="fa-brands fa-spotify" style="color: #2bdae1;"></i>
              </a></li>
          
          
              <li><a href="https://twitter.com/imaginedragons">
                  <i class="fa-brands fa-twitter" style="color: #2bdae1;">
              </i></a></li>
         
         
              <li><a href="https://www.youtube.com/imaginedragons"><i class="fa-brands fa-square-youtube" style="color: #2bdae1;">
                  </i></a></li>
          
          
              <li><a href="https://www.instagram.com/imaginedragons/"><i class="fa-brands fa-instagram" style="color: #2bdae1;">
                  </i></a></li>
          </ul>
      </nav>

     
  </header>
      `;
    }
  }

  customElements.define('main-header', Header);