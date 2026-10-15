import { Routes, Route, Link } from 'react-router-dom';
import ProfilePage from './pages/ProfilePage';
import BusinessPage from './pages/BusinessPage';

export default function App() {
  return (
    <div className='p-5'>
      <Routes>
        <Route path="/" element={<ProfilePage/>} />
        <Route path="/business/:id" element={<BusinessPage />} />
      </Routes>
    </div>
  )
}