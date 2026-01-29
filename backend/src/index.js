const app = require('./app');
const { ensureStorage } = require('./utils/storage');

const PORT = process.env.PORT || 3000;

// Initialize storage
try {
  ensureStorage();
} catch (error) {
  console.warn('Storage initialization skipped:', error.message);
}

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
