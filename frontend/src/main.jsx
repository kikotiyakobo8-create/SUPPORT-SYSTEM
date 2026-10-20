import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './styles.css'
import './signout.css'
import './language.css'
import './portal-header.css'
import './login-hero.css'
import './queue-filters.css'

createRoot(document.getElementById('root')).render(<StrictMode><App /></StrictMode>)
