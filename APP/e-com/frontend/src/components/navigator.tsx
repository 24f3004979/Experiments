import React from 'react';
import logo from '../assets/logo.svg'

export default function Header(): React.JSX.Element {
  return (
    <div id='navigation'>
      < header >
        <nav style={styles.nav}>
          <img style={styles.img} src={logo} />
          <a>HOME</a>
          <a>ORDERS</a>
          <a>USER</a>
        </nav>
      </header>
    </div>
  );
}

// style element is here for the styling
const styles = {
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px 40px',
    backgroundColor: 'blue',
    borderBottom: '1px solid #ddd',
  },
  img: {
    width: '3rem',
    height: '3rem',
    borderRadius: '5px'
  },
  nav: {
    display: 'flex',
    gap: '20px',
    backgroundColor: 'hsl(0,0%, 10%)',
    height: '4rem',
    width: '20rem',
    justifyContent: 'center',
    alignItems: 'center',
    color: 'white',
    borderRadius: '10px'
  },
  link: {
    textDecoration: 'none',
    color: '#0070f3',
    fontWeight: '500',
  },
};
