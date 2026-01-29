const express = require('express');
const cors = require('cors');
const assessRoutes = require('./api/assess');

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api/assess', assessRoutes);

module.exports = app;
