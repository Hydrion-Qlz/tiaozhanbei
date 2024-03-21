<template>
    <div id="container">
        <div class="text-container">
            <p>基于知识图谱的企业风险预测系统</p>
            <a-button @click="toSearch" class="button">开启探索</a-button>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            author: {
                name: 'John Doe',
                books: ['Vue 2 - Advanced Guide', 'Vue 3 - Basic Guide', 'Vue 4 - The Mystery'],
            },
        };
    },
    methods: {
        toSearch() {
            console.log('go to search');
            this.$router.push({
                name: 'search',
            });
        },
    },
};
</script>

<style scoped>
#container {
    width: 100%;
    height: 100%;
    position: absolute;
    background: url('@/assets/bk3.jpg');
    background-position: 100% 100%;
    background-size: 100% auto;
}
.text-container {
    width: 600px;
    margin: 0 auto;
    text-align: center;
    margin-top: 200px;
}
p {
    color: white;
    font-size: 40px;
}
.button {
    background-color: transparent;
    border: 1px solid #ffffff;
    color: #ffffff;
    font-size: 20px;
    padding: 12px 50px;
    width: 280px;
    height: 56px;
    margin: o auto;
    text-align: center;
}
</style>
