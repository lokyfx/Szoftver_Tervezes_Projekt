import { useState } from 'react'
import RiderDashboard from './RiderDashboard.jsx'
import RestaurantDashboard from './RestaurantDashboard.jsx'
import './App.css'

function App() {
  const [view, setView] = useState('restaurant')

  return (
    <>
      <nav style={{ position: 'fixed', zIndex: 2000, top: 14, right: 20 }}>
        <button type="button" onClick={() => setView('rider')}>Rider</button>
        <button type="button" onClick={() => setView('restaurant')}>Restaurant</button>
      </nav>
      {view === 'rider' ? <RiderDashboard /> : <RestaurantDashboard />}
    </>
  )
}

export default App
