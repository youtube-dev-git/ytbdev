<template>
        <div class="contains">
            <div class="card">
            <h1>{{event.title}}</h1>
            <span>{{event.attend.length}} attend</span>
            </div>
        </div>
</template>
<script>
export default {

    props:{
        event: Object
    }
}
</script>
<style scoped>
.contains{
    display: flex;
    justify-content: center;
}
.card{
   box-shadow: 2px 2px 2px 2px rgb(68, 67, 66);
   color: black;
   width: 300px;
}
span{
    color: rgb(26, 25, 25);
    margin-top: 20px;
}
</style>
