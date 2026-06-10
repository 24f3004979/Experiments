import React from 'react';
import logo from '../assets/logo.png'

export default function Header(): React.JSX.Element {
  return (
    < header >
      <img style={styles.img} src={logo} />
      <nav style={styles.nav}>
        <a styles={styles.link} >HOME</a>
        <a>ORDERS</a>
        <a>PROFILE</a>
      </nav>
    </header>
  );
}

// style element is here for the styling
const styles = {
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px 40px',
    backgroundColor: '#f8f9fa',
    borderBottom: '1px solid #ddd',
  },
  img: {
    width: '5rem',
    height: '4rem'
  },
  nav: {
    display: 'flex',
    gap: '20px',
  },
  link: {
    textDecoration: 'none',
    color: '#0070f3',
    fontWeight: '500',
  },
};
