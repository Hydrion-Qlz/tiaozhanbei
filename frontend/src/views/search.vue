<template>
    <div id="container">this is the search page</div>
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
        },
    },
};
</script>

<style scoped>
#container {
    width: 100%;
    height: 100%;
    position: absolute;
    /* background: url('@/assets/bk3.jpg'); */
    background-position: 100% 100%;
    background-size: 100% auto;
}
</style>
