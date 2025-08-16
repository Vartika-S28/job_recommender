# 🎯 Job Recommender System

A modern, AI-powered job recommendation system that helps users find their perfect job matches by analyzing their skills and resume. Built with Flask, Python, and advanced machine learning algorithms.

![Job Recommender](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Machine Learning](https://img.shields.io/badge/ML-TF--IDF-orange.svg)
![Responsive](https://img.shields.io/badge/Responsive-Yes-brightgreen.svg)

## ✨ Features

### 🤖 AI-Powered Matching
- **Advanced TF-IDF Algorithm**: Uses sophisticated text analysis to match skills
- **Cosine Similarity**: Provides accurate job-skill matching scores
- **Resume Parsing**: Automatically extracts skills from PDF resumes
- **Real-time Analysis**: Instant job recommendations

### 🎨 Modern UI/UX
- **Full-Page Design**: Immersive, modern interface
- **Glassmorphism Effects**: Beautiful backdrop blur and transparency
- **Responsive Layout**: Works perfectly on all devices
- **Smooth Animations**: Engaging user interactions
- **Professional Styling**: Clean, modern design with gradients

### 📱 User Experience
- **Dual Input Methods**: Upload resume or manually enter skills
- **Flash Notifications**: Real-time feedback and status updates
- **Loading States**: Visual feedback during processing
- **Auto-hide Messages**: Clean interface with timed notifications
- **Session Management**: Secure user authentication

### 🔧 Technical Features
- **PDF Processing**: Automatic text extraction from resumes
- **Error Handling**: Robust error management and user feedback
- **Scalable Architecture**: Easy to extend and modify
- **Clean Code**: Well-structured, maintainable codebase

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/job_recommender.git
   cd job_recommender
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📖 Usage Guide

### Getting Started
1. **Login**: Enter your name to start using the application
2. **Choose Input Method**:
   - **Option 1**: Upload your PDF resume for automatic skill extraction
   - **Option 2**: Manually enter your skills and technologies
3. **Get Recommendations**: Click "Find My Perfect Job" to receive personalized matches
4. **Review Results**: Browse through your top job matches with required skills

### Input Examples
- **Skills**: `Python, SQL, Machine Learning, Data Analysis, Excel, JavaScript, React, Node.js`
- **Resume**: Upload any PDF resume file

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for Python
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **PyMuPDF (fitz)**: PDF processing and text extraction

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: Interactive functionality
- **Google Fonts**: Inter font family

### Machine Learning
- **TF-IDF Vectorization**: Text feature extraction
- **Cosine Similarity**: Similarity scoring algorithm
- **Natural Language Processing**: Skill matching and analysis

## 📁 Project Structure

```
job_recommender/
├── app.py                 # Main Flask application
├── jobs.csv              # Job dataset with titles and required skills
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore file
├── static/
│   └── style.css        # Modern CSS styling
└── templates/
    ├── index.html       # Main application page
    └── login.html       # Login page
```

## 🔧 Configuration

### Environment Variables
The application uses a simple secret key for session management. For production, consider using environment variables:

```python
# In app.py
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key')
```

### Customizing Job Data
To add more jobs, simply update the `jobs.csv` file:

```csv
Job Title,Required Skills
Software Engineer,Python, JavaScript, React, Node.js
Data Scientist,Python, SQL, Machine Learning, Statistics
Product Manager,Agile, Scrum, User Research, Analytics
```

## 🎨 Customization

### Styling
The application uses modern CSS with:
- **CSS Grid**: Responsive layouts
- **Flexbox**: Flexible component positioning
- **CSS Variables**: Easy color customization
- **Animations**: Smooth transitions and effects

### Adding Features
The modular structure makes it easy to add new features:
- **New ML Algorithms**: Extend the recommendation engine
- **Additional Data Sources**: Connect to job APIs
- **User Profiles**: Add user account management
- **Job Applications**: Integrate application tracking

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider using:
- **Gunicorn**: WSGI server
- **Nginx**: Reverse proxy
- **Docker**: Containerization
- **Cloud Platforms**: Heroku, AWS, Google Cloud

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask Community**: For the excellent web framework
- **Scikit-learn**: For powerful machine learning tools
- **Google Fonts**: For beautiful typography
- **CSS Community**: For modern styling techniques

## 📞 Support

If you have any questions or need help:
- Create an issue in the repository
- Contact: [your-email@example.com]
- Documentation: [Link to docs]

---

**Made with ❤️ by [Your Name]**

*Transform your job search with AI-powered recommendations!*
