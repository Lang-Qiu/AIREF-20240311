const fs = require('fs');
const path = require('path');

const USER_DATA_DIR = path.join(__dirname, '../../../UserData');

const ensureStorage = () => {
    if (!fs.existsSync(USER_DATA_DIR)) {
        fs.mkdirSync(USER_DATA_DIR, { recursive: true });
    }
};

module.exports = { USER_DATA_DIR, ensureStorage };
