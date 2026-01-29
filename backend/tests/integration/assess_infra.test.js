import { describe, it, expect } from 'vitest';
import request from 'supertest';
import fs from 'fs';
import path from 'path';
import app from '../../src/app';
import { USER_DATA_DIR, ensureStorage } from '../../src/utils/storage';

describe('REQ-101: Assess Module Infrastructure', () => {
    
    it('Scenario 1: Verify Route Mounting - GET /api/assess/health', async () => {
        const response = await request(app).get('/api/assess/health');
        expect(response.status).toBe(200);
        expect(response.body).toEqual({ status: 'ok' });
    });

    it('Scenario 2: Verify Storage Directory', () => {
        // Run implementation logic
        try {
            ensureStorage();
        } catch (e) {
            // If it throws, test might fail depending on expectation
        }
        
        const exists = fs.existsSync(USER_DATA_DIR);
        expect(exists).toBe(true);
        
        // Check write permission
        if (exists) {
            const testFile = path.join(USER_DATA_DIR, 'test_write.txt');
            fs.writeFileSync(testFile, 'test');
            expect(fs.existsSync(testFile)).toBe(true);
            fs.unlinkSync(testFile);
        }
    });
});
