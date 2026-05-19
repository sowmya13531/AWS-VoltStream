import { Link } from 'react-router-dom';
import { AlertCircle } from 'lucide-react';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center h-full animate-in fade-in zoom-in-95 duration-500">
      <div className="bg-slate-900 border border-slate-800 p-12 rounded-3xl shadow-2xl flex flex-col items-center text-center">
        <div className="bg-rose-500/20 p-4 rounded-full mb-6">
          <AlertCircle className="w-12 h-12 text-rose-400" />
        </div>
        <h1 className="text-6xl font-bold text-slate-100 mb-4">404</h1>
        <h2 className="text-2xl font-semibold text-slate-300 mb-2">Page Not Found</h2>
        <p className="text-slate-400 mb-8 max-w-sm">
          The page you are looking for doesn't exist or has been moved.
        </p>
        <Link 
          to="/" 
          className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-8 rounded-xl transition-colors shadow-lg shadow-blue-500/30"
        >
          Return to Dashboard
        </Link>
      </div>
    </div>
  );
}
