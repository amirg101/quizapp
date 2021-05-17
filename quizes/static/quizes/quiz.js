console.log("heyworld");
const url =window.location.href;
const resultBox=document.getElementById('result-box');
const scoreBox=document.getElementById('score-box');

const quizbox = document.getElementById('quiz');
// $.ajax({
//     type:'GET',
//     url:`${url}data`,
//     success:function(response){
//         console.log(response);
//         const data = response.data; 
//         data.forEach(el => {
//             // for (const[question,answers] of Object.entries(el)){
//             //   quizbox.innerHTML +=`
//             //   <hr>
//             //   <div class="mb-2">
//             //   ⌛ <b class="h3">${question} :</b> 
//             //   </div>

//             //   `  
//             //   answers.forEach(answer=>{
//             //       quizbox.innerHTML+=`
//             //       <div>
//             //       <input type="radio" style="margin:5px" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
//             //       <label for="${question}" class="h6">${answer}</label>
//             //       </input>
//             //       </div>
//             //       `
//             //   })
//             }   

//         });


//     },
//     error:function(error){
//         console.log(error)
//     }
// })  

const quizForm=document.getElementById('quiz-form');
const csrf=document.getElementsByName('csrfmiddlewaretoken');

const sendData=()=>{
    const elements=[...document.getElementsByClassName('ans')]

    const data={}
    data['csrfmiddlewaretoken']=csrf[0].value
    elements.forEach(el => {
        if (el.checked){
            data[el.name]=el.value;
        }
        else{
            if (!data[el.name]){
                data[el.name]=null
            }
        }
    });
    $.ajax({
        type:'POST',
        url:`${url}save/`,
        data: data,
        success:function(response){
            const results =response.results
            quizForm.classList.add('not-visible')
            scoreBox.innerHTML=`${response.passed ? '<h3>Congratulations!! </h3>' : ' <h3> oops....'} your result is ${response.score.toFixed(2)}% </h3>`
            results.forEach(res=>{
                const resDiv=document.createElement("div")
                for (const [question , resp] of Object.entries(res)){
                    // console.log(question)
                    // console.log(response);
                    // console.log('*******');
                    resDiv.innerHTML+=question
                    const cls=['container','p-3','text-light','h6']
                    resDiv.classList.add(...cls)
                    if (resp=='not answered'){
                        resDiv.innerHTML+="- not answered"
                        resDiv.classList.add('bg-danger')
                    }
                    else{
                        const answer=resp['answered']
                        const correct=resp['correct_answer']
                        if (answer==correct){
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML+=` |  answered: ${answer}`

                        }
                        else{
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML+=` | correct answer: ${correct}`
                            resDiv.innerHTML+=` | answered: ${answer}`   
                        }

                    }
                }
                // const body = document.getElementsByTagName('body')[0]
                resultBox.append(resDiv)

            })
        },
        error:function(error){
            console.log(error)
        },

    })
}
quizForm.addEventListener('submit',e=>{
    e.preventDefault()

    sendData()
})