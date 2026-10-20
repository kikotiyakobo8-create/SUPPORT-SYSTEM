import { useEffect, useState } from 'react'
import './accessibility.css'

const saved = (key, fallback) => localStorage.getItem(key) || fallback

export default function AccessibilityMenu({ locale, setLocale }) {
  const [open, setOpen] = useState(false)
  const [theme, setTheme] = useState(() => saved('tsms_theme', 'system'))
  const [contrast, setContrast] = useState(() => saved('tsms_contrast_mode', 'normal'))
  const [customContrast, setCustomContrast] = useState(() => Number(saved('tsms_custom_contrast', '100')))
  const [textSize, setTextSize] = useState(() => saved('tsms_text_size', 'normal'))

  useEffect(() => {
    const handleKey = event => {
      if (event.ctrlKey && event.key.toLowerCase() === 'u') { event.preventDefault(); setOpen(value => !value) }
      if (event.key === 'Escape') setOpen(false)
    }
    window.addEventListener('keydown', handleKey)
    return () => window.removeEventListener('keydown', handleKey)
  }, [])

  useEffect(() => {
    localStorage.setItem('tsms_theme', theme)
    const resolved = theme === 'system' ? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light') : theme
    document.documentElement.dataset.theme = resolved
  }, [theme])

  useEffect(() => {
    localStorage.setItem('tsms_contrast_mode', contrast)
    const filters = { normal: 'none', inverted: 'invert(1) hue-rotate(180deg)', dark: 'contrast(1.15) brightness(.78)', light: 'contrast(1.08) brightness(1.16)' }
    document.documentElement.style.setProperty('--accessibility-filter', contrast === 'custom' ? `contrast(${customContrast}%)` : filters[contrast])
  }, [contrast, customContrast])

  useEffect(() => {
    localStorage.setItem('tsms_custom_contrast', String(customContrast))
  }, [customContrast])

  useEffect(() => {
    localStorage.setItem('tsms_text_size', textSize)
    document.documentElement.dataset.textSize = textSize
  }, [textSize])

  const chooseLocale = value => { setLocale(value); localStorage.setItem('tsms_language', value) }
  const Choice = ({ active, onClick, icon, children }) => <button className={`access-choice${active ? ' selected' : ''}`} onClick={onClick}>{active && <b>✓</b>}<span className="choice-icon">{icon}</span><span>{children}</span></button>

  return <div className="accessibility"><button className="accessibility-trigger" onClick={() => setOpen(value => !value)} aria-expanded={open} aria-controls="accessibility-panel" title="Accessibility menu (Ctrl+U)"><span>♿</span><span className="accessibility-label">Accessibility</span></button>{open && <section id="accessibility-panel" className="accessibility-panel" aria-label="Accessibility Menu"><header><div className="accessibility-symbol">♿</div><div><strong>Accessibility Menu <em>(CTRL+U)</em></strong><span>Customize your experience</span></div><button onClick={() => setOpen(false)} aria-label="Close accessibility menu">×</button></header><div className="accessibility-body"><Group title="LANGUAGE"><Choice active={locale === 'en'} onClick={() => chooseLocale('en')} icon="🇬🇧">English (EN)</Choice><Choice active={locale === 'sw'} onClick={() => chooseLocale('sw')} icon="🇹🇿">Kiswahili (SW)</Choice></Group><Group title="THEME"><Choice active={theme === 'system'} onClick={() => setTheme('system')} icon="▣">System</Choice><Choice active={theme === 'light'} onClick={() => setTheme('light')} icon="☼">Light</Choice><Choice active={theme === 'dark'} onClick={() => setTheme('dark')} icon="☾">Dark</Choice></Group><Group title="CONTRAST"><Choice active={contrast === 'normal'} onClick={() => setContrast('normal')} icon="◉">Normal</Choice><Choice active={contrast === 'inverted'} onClick={() => setContrast('inverted')} icon="◉">Inverted</Choice><Choice active={contrast === 'dark'} onClick={() => setContrast('dark')} icon="☾">Dark</Choice><Choice active={contrast === 'light'} onClick={() => setContrast('light')} icon="☼">Light</Choice></Group><div className="slider-heading"><span>CUSTOM CONTRAST</span><strong>{customContrast}%</strong></div><input className="contrast-slider" type="range" min="75" max="150" value={customContrast} onChange={e => { setCustomContrast(Number(e.target.value)); setContrast('custom') }} /><div className="slider-scale"><span>SUBTLE</span><span>NORMAL</span><span>HIGH</span></div><Group title="TEXT SIZE"><Choice active={textSize === 'normal'} onClick={() => setTextSize('normal')} icon="">Normal</Choice><Choice active={textSize === 'small'} onClick={() => setTextSize('small')} icon="">S</Choice><Choice active={textSize === 'large'} onClick={() => setTextSize('large')} icon="">L</Choice><Choice active={textSize === 'xl'} onClick={() => setTextSize('xl')} icon="">XL</Choice><Choice active={textSize === 'xxl'} onClick={() => setTextSize('xxl')} icon="">XXL</Choice></Group></div></section>}</div>
}

function Group({ title, children }) { return <section className="access-group"><h3>{title}</h3><div className="access-options">{children}</div></section> }
