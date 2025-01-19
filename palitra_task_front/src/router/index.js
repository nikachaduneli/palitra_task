import {createRouter, createWebHistory} from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import PostDetail from '@/views/PostDetail.vue';
import ProfileEditPage from "@/views/ProfileEditPage.vue";
import ProfilePage from "@/views/ProfilePage.vue";
import BlogFormPage from "@/views/BlogFormPage.vue";

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/blog/:id',
        name: 'PostDetail',
        component: PostDetail,
        props: true
    },
    {
        path: '/profile/edit',
        name: 'ProfileEdit',
        component: ProfileEditPage
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfilePage
    },
    {
        path: '/blog/edit/:blogId?',
        name: 'BlogFormEdit',
        component: BlogFormPage,
    },
    {
        path: '/blog/create/',
        name: 'BlogForm',
        component: BlogFormPage,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
