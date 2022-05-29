import './App.css';
import './components/FileUpload.js'
import FileUpload from './components/FileUpload.js';

 const App = ()=> (
   <div className="container mt-4">
     <h4 className="display-4 text-center mb-4">FaceBlock</h4>
     <FileUpload label="Upload Image"/> 
   </div>

  );

export default App;
