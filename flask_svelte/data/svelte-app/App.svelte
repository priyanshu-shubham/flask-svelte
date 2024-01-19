<script>
	export let greetings;
</script>

<main class="flex flex-col items-center justify-center h-screen w-screen bg-neutral-900 text-white">
	<div class="p-10 border border-red-500 rounded-lg hover:bg-black">
		<h1 class="text-3xl text-red-500 font-bold tracking-tight text-center mb-5">
			{greetings} from
			{document.data.name}
		</h1>
		<p class="mb-2">
			Visit the <a href="https://svelte.dev/tutorial" class="text-blue-600"
				>Svelte tutorial</a> to learn how to build Svelte apps.
		</p>
		<p>
			Also, Visit the <a
				href="https://github.com/priyanshu-shubham/flask-svelte"
				class="text-blue-600">Flask Svelte</a> documentation to learn how to use Flask Svelte.
		</p>
	</div>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>
