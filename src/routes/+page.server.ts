import type { PageLoad } from './$types';
import { API_KEY } from '$env/static/private';

export const load: PageLoad = () => {
  return {
    title: 'Plain Map',
    apiKey: API_KEY,
  };
};
