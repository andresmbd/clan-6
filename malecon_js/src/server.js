import express from 'express'


const app = express()

//Read
app.get('/coders', (req, res)=>{
    res.json([
        {
            id:1,
            name:'Didian',
            age: 34,
            status:true
        }
    ])
    res.send('Hey aqui van los coders')
})

export default app;