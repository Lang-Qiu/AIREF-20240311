import Vue from 'vue'
import VueRouter from 'vue-router'

import Layout from '@/views/layout'
import Home from '@/views/home'
import Login from '@/views/login'
import Register from '@/views/register'
import Show from '@/views/show'
import ModelList from '@/views/modellist'
import DataBase from '@/views/database'
import ModelAssess from '@/views/modelassess'
import Data from '@/views/modelassess/data'
import Model from '@/views/modelassess/model'
import Attack from '@/views/modelassess/attack'
import Backdoor from '@/views/backdoor'
import Compete from '@/views/compete'
import Frame from '@/views/frame'
import Report from '@/views/report'
import Strengthen from '@/views/strengthen'
import Audio from '@/views/modelassess/audio'
import Image from '@/views/modelassess/image'
import Knowledge from '@/views/modelassess/knowledge'
import Reinforce from '@/views/modelassess/reinforce'
import Tab from '@/views/modelassess/tab'
import Text from '@/views/modelassess/text'
import Visual from '@/views/modelassess/visual'
import Sketch from '@/views/modelassess/sketch'

Vue.use(VueRouter)
const routes = [
    {
        path: '/',
        component: Layout,
        redirect: '/home',
        children: [
            {
                path: 'home',
                component: Home
            },
            {
                path: 'show',
                name: 'show',
                component: Show
            },
            {
                path: 'modelassess',
                name: 'modelassess',
                redirect: '/modelassess/sketch',
                component: ModelAssess,
                
                children: [
                    {
                        path: 'sketch',
                        component: Sketch,                        
                    },
                    {
                        path: 'image',
                        component: Image,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'audio',
                        component: Audio,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'knowledge',
                        component: Knowledge,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'reinforce',
                        component: Reinforce,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'tab',
                        component: Tab,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'text',
                        component: Text,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                    {
                        path: 'visual',
                        component: Visual,                        
                        children: [
                            {
                                path: 'data',
                                component: Data
                            },
                            {
                                path: 'model',
                                component: Model
                            },
                            {
                                path: 'attack',
                                component: Attack
                            }
                        ]
                    },
                ]
            },
            {
                path: 'database',
                component: DataBase
            },
            
            {
                path: 'modellist',
                component: ModelList
            },
            {
                path: 'backdoor',
                component: Backdoor,
                redirect: '/backdoor/data',
                children: [
                    {
                        path: 'data',
                        component: Data
                    },
                    {
                        path: 'model',
                        component: Model,
                    },
                    {
                        path: 'attack',
                        component: Attack
                    }
                ]
            },
            {
                path: 'compete',
                component: Compete,
                redirect: '/compete/data',
                children: [
                    {
                        path: 'data',
                        component: Data
                    },
                    {
                        path: 'model',
                        component: Model,
                    },
                    {
                        path: 'attack',
                        component: Attack
                    }
                ]
            },
            {
                path: 'frame',
                component: Frame
            },
            {
                path: 'report',
                component: Report
            },
            {
                path: 'strengthen',
                component: Strengthen,
                redirect: '/strengthen/data',
                children: [
                    {
                        path: 'data',
                        component: Data
                    },
                    {
                        path: 'model',
                        component: Model,
                    },
                    {
                        path: 'attack',
                        component: Attack
                    }
                ]
            },
            
        ]
    },

    {
        path: '/login',
        name: 'login',
        component: Login
    },

    {
        path: '/register',
        name: 'register',
        component: Register
    },

    
    
]

const router = new VueRouter({
    mode: 'history',
    // base: '/show/',
    base: process.env.BASE_URL,
    routes
})


export default router 